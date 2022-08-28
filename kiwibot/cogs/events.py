import discord, json, requests, os, asyncio, random
from discord import Option
from discord.ext import commands
from discord.commands import option
from PIL import Image, ImageDraw, ImageFont, ImageChops
from io import BytesIO

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    with open("kiwibot/json/description.json", "r") as dfile:
      cmdsdescription = json.load(dfile)
  
    @commands.Cog.listener()
    async def on_ready(self):
      print("cmds.events loaded")
      await self.bot.db.execute("CREATE TABLE IF NOT EXISTS welcome (guildid BIGINT, channelid BIGINT, roleid BIGINT, messagetype TEXT, message TEXT)")
      await self.bot.db.execute("CREATE TABLE IF NOT EXISTS goodbye (guildid BIGINT, channelid BIGINT, messagetype TEXT, message TEXT)")


    # ON MEMBER REMOVE
    @commands.Cog.listener()
    async def on_member_remove(self, member):
      goodbyeFetch = await self.bot.db.fetch('SELECT * FROM goodbye WHERE guildid = $1', member.guild.id)
      if len(goodbyeFetch) != 0:
        channel = self.bot.get_channel(goodbyeFetch[0]['channelid'])
        if channel:
          message = goodbyeFetch[0]['message']

          message = message.replace("<guild.name>", member.guild.name) if "<guild.name>" in str(message) else message
          message = message.replace("<member.mention>", member.mention) if "<member.mention>" in str(message) else message
          message = message.replace("<member.name>", f"{member.name}#{member.discriminator}") if "<member.name>" in str(message) else message

          await channel.send(message)

    # ON MEMBER JOIN
    @commands.Cog.listener()
    async def on_member_join(self, member):

      def circle(pfp,size = (215,215)):       
        pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
        
        bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
        mask = Image.new('L', bigsize, 0)
        draw = ImageDraw.Draw(mask) 
        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(pfp.size, Image.ANTIALIAS)
        mask = ImageChops.darker(mask, pfp.split()[-1])
        pfp.putalpha(mask)
        return pfp

      welcomeFetch = await self.bot.db.fetch('SELECT * FROM welcome WHERE guildid = $1', member.guild.id)
      if len(welcomeFetch) != 0:
        channel = self.bot.get_channel(welcomeFetch[0]['channelid'])
        role = member.guild.get_role(welcomeFetch[0]['roleid'])

        if role:
          await member.add_roles(role)
          
        if channel:
          message = welcomeFetch[0]['message']
          message_type = welcomeFetch[0]['messagetype']

          message = message.replace("<guild.name>", member.guild.name) if "<guild.name>" in str(message) else message
          message = message.replace("<member.mention>", member.mention) if "<member.mention>" in str(message) else message
          message = message.replace("<member.name>", f"{member.name}#{member.discriminator}") if "<member.name>" in str(message) else message

          if message_type == "Text":
            await channel.send(message)

          else:
              welcome = Image.new(mode="RGBA", size=(1000, 460), color = (0, 0, 0, 190))
              
              keyword = random.choice(["forest", "city", "mountains", "romania"])
              bresponse = requests.get(f"https://source.unsplash.com/random/1000x460/?{keyword}")
              
              background = Image.open(BytesIO(bresponse.content))
              background =  background.convert('RGB')  
              background.paste(welcome, (0, 0), welcome)
              
              aresponse = requests.get(member.avatar.url)
              avatar = Image.open(BytesIO(aresponse.content))
              avatar = avatar.resize((256, 256))
              avatar = circle(avatar, (256, 256))
  
              background.paste(avatar, (380, 70), avatar)
              
              textimg = ImageDraw.Draw(background)
        
              font = ImageFont.truetype("kiwibot/fonts/Roboto-Light.ttf", 35)
              textimg.text((500, 370), f"Welcome, {member.name}#{member.discriminator}!", font=font, anchor="mm")  
              
              background.save(f'welcome{member.name}.png')     
              file=discord.File(f'welcome{member.name}.png')
            
              await channel.send(message, file=file)
              await asyncio.sleep(1)
              os.remove(f"welcome{member.name}.png")

    # EVENTS COMMANDS #######################

    #SETUP
    @commands.slash_command(name="setup", description=f"{cmdsdescription['setup']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    @option(
      "type",
      autocomplete=discord.utils.basic_autocomplete(["Default Role", "Welcome", "Goodbye"]),
    )

    @option(
      "message_type",
      default=None,
      description="The message type 'Image' is used only in 'Welcome' type..",
      autocomplete=discord.utils.basic_autocomplete(["Text", "Image"]),
    )
    async def setup(self, ctx,
      type : str,
      role : Option(discord.Role, required=False),
      channel : Option(discord.TextChannel, required=False),
      message_type : str,
      message : Option(str, description="<guild>-name of the guild <member.mention>-mention the member <member.name>-name of the member", required=False),
    ):
      embed = discord.Embed(color=discord.Colour.blue(), title="Setup", description="Something went wrong. Please try again!")

      if ctx.author.guild_permissions.administrator: 
        #Default role when a user joins the server
        if type == "Default Role":
          if role != None:
            roleFetch = await self.bot.db.fetch('SELECT * FROM welcome WHERE guildid = $1', ctx.guild.id)
            if len(roleFetch) == 0:
              await self.bot.db.execute('INSERT INTO welcome(guildid, roleid) VALUES ($1, $2)', ctx.guild.id, role.id)

            else:
              await self.bot.db.execute('UPDATE welcome SET roleid = $1 WHERE guildid = $2', role.id, ctx.guild.id)

            embed.description = f"The default role was set to '{role.name}'"

          else:
            embed.title = "Error"
            embed.description = "The option 'role' needs to be filled."

        #Welcome message
        if type == "Welcome":
          if channel != None and message_type != None and message != None:
            welcomeFetch = await self.bot.db.fetch('SELECT * FROM welcome WHERE guildid = $1', ctx.guild.id)
            if len(welcomeFetch) == 0:
              await self.bot.db.execute('INSERT INTO welcome(guildid, channelid, messagetype, message) VALUES ($1, $2, $3, $4)', ctx.guild.id, channel.id, message_type, message)

            else:
              await self.bot.db.execute('UPDATE welcome SET channelid = $1, messagetype = $2, message = $3 WHERE guildid = $4', channel.id, message_type,  message, ctx.guild.id)

            embed.description = f"**Channel** \n'{channel.name}' \n**Message Type** \n{message_type} \n**Message**\n'{message}'"
            
          else:
            embed.title = "Error"
            embed.description = "The options 'channel', 'messagetype', 'message' need to be filled."

        #Goodbye message
        if type == "Goodbye":
          if channel != None and message_type != None and message != None:
            goodbyeFetch = await self.bot.db.fetch('SELECT * FROM goodbye WHERE guildid = $1', ctx.guild.id)
            if len(goodbyeFetch) == 0:
              await self.bot.db.execute('INSERT INTO goodbye(guildid, channelid, messagetype, message) VALUES ($1, $2, $3, $4)', ctx.guild.id, channel.id, message_type, message)

            else:
              await self.bot.db.execute('UPDATE goodbye SET channelid = $1, messagetype = "Text", message = $2 WHERE guildid = $3', channel.id,  message, ctx.guild.id)

            embed.description = f"**Channel** \n'{channel.name}' \n**Message Type** \n'Text' \n**Message**\n'{message}'"

          else:
            embed.title = "Error"
            embed.description = "The options 'channel', 'message_type', 'message' need to be filled."


      await ctx.respond(embed=embed)
      
def setup(bot):
    bot.add_cog(Events(bot))
