import discord, sqlite3, json, random, requests, asyncio, os
from discord import Option
from discord.ext import commands
from discord.commands import SlashCommandGroup, option
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
from io import BytesIO

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    with open("kiwibot/json/description.json", "r") as dfile:
      cmdsdescription = json.load(dfile)
      
    setup = SlashCommandGroup("setup", "Commands related to setup")
  
    @commands.Cog.listener()
    async def on_ready(self):
      print("cmds.events loaded")

      #########################
      ## WELCOME & DEFAULT ROLE
      ##########
      
      conn = sqlite3.connect("kiwibot/database/welcome.db")
      cursor = conn.cursor()

      cursor.execute("CREATE TABLE IF NOT EXISTS welcome (guildid INTEGER, channelid INTEGER, type TEXT, message TEXT);")
      cursor.execute("CREATE TABLE IF NOT EXISTS defaultrole (guildid INTEGER, roleid INTEGER);")

      conn.commit()
      conn.close()
      
      #########################
      ## GOODBYE
      ##########
      
      conn = sqlite3.connect("kiwibot/database/goodbye.db")
      cursor = conn.cursor()

      cursor.execute("CREATE TABLE IF NOT EXISTS goodbye (guildid INTEGER, channelid INTEGER, message TEXT);")

      conn.commit()
      conn.close()

    # ON MEMBER REMOVE
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        conn = sqlite3.connect("kiwibot/database/goodbye.db")
        cursor = conn.cursor()
          
        cursor.execute("SELECT * FROM goodbye WHERE guildid = ?", (member.guild.id,))
        data = cursor.fetchone()

        if data:
          channel = self.bot.get_channel(data[1])
          if channel:
            goodbyemsg = data[2]

            goodbyemsg = goodbyemsg.replace("<guild.name>", member.guild.name) if "<guild.name>" in str(goodbyemsg) else goodbyemsg
            goodbyemsg = goodbyemsg.replace("<member.mention>", member.mention) if "<member.mention>" in str(goodbyemsg) else goodbyemsg
            goodbyemsg = goodbyemsg.replace("<member.name>", f"{member.name}#{member.discriminator}") if "<member.name>" in str(goodbyemsg) else goodbyemsg
  
            await channel.send(goodbyemsg)


        conn.commit()
        conn.close()   

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

        conn = sqlite3.connect("kiwibot/database/welcome.db")
        cursor = conn.cursor()
      
        cursor.execute("SELECT * FROM defaultrole WHERE guildid = ?", (member.guild.id,))
        rdata = cursor.fetchone()
        if rdata:
          role = member.guild.get_role(rdata[1])
          if role:
            await member.add_roles(role)
      
        cursor.execute("SELECT * FROM welcome WHERE guildid = ?", (member.guild.id,))
        data = cursor.fetchone()

        if data:
          channel = self.bot.get_channel(data[1])
  
          if channel:
            welcomemsg = data[3]
      
            welcomemsg = welcomemsg.replace("<guild.name>", member.guild.name) if "<guild.name>" in str(welcomemsg) else welcomemsg
            welcomemsg = welcomemsg.replace("<member.mention>", member.mention) if "<member.mention>" in str(welcomemsg) else welcomemsg
            welcomemsg = welcomemsg.replace("<member.name>", f"{member.name}#{member.discriminator}") if "<member.name>" in str(welcomemsg) else welcomemsg
  
            if data[2] == "Text":
              await channel.send(welcomemsg)
  
            if data[2] == "Image":
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
            
              await channel.send(welcomemsg, file=file)
              await asyncio.sleep(1)
              os.remove(f"welcome{member.name}.png")

        conn.commit()
        conn.close()         

    # EVENTS COMMANDS #######################
      
    #GOODBYE SETUP
    @setup.command(name="goodbye", description=f"{cmdsdescription['goodbyesetup']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def goodbyesetup(self, ctx, channel : Option(discord.TextChannel, required=True), message : Option(str, description="<guild>-name of the guild <member.mention>-mention the member <member.name>-name of the member", required=True)):
      embed = discord.Embed(
        title="Goodbye Setup",
        color=discord.Colour.blue()
      )
      
      if ctx.author.guild_permissions.administrator: 
      
        conn = sqlite3.connect("kiwibot/database/goodbye.db")
        cursor = conn.cursor()
  
        cursor.execute("SELECT * FROM goodbye WHERE guildid = ?", (ctx.guild.id,))
        data = cursor.fetchone()
  
        if data:
          cursor.execute("UPDATE goodbye SET channelid = ?, message = ? WHERE guildid = ?", (channel.id, message, ctx.guild.id,))
          embed.description="Data succesfully updated!"
          
        else:
          cursor.execute("INSERT INTO goodbye VALUES (?, ?, ?)", (ctx.guild.id, channel.id, message,))
          embed.description="Data succesfully inserted!"
  
        conn.commit()
        conn.close()
        
      else:
        embed.title = "Error"
        embed.description = "You can't use this command. Missing permission 'Administrator'"
        
      await ctx.respond(embed=embed)

    #WELCOME SETUP
    @setup.command(name="welcome", description=f"{cmdsdescription['welcomesetup']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    @option(
        "type",
        autocomplete=discord.utils.basic_autocomplete(["Text", "Image"]),
    )
    async def welcomesetup(self, ctx, channel : Option(discord.TextChannel, required=True), type : str, message : Option(str, description="<guild.name>-name of the guild <member.mention>-mention the member <member.name>-name of the member", required=True)):
      embed = discord.Embed(
        title="Welcome Setup",
        color=discord.Colour.blue()
      )
      if ctx.author.guild_permissions.administrator: 
      
        conn = sqlite3.connect("kiwibot/database/welcome.db")
        cursor = conn.cursor()
  
        cursor.execute("SELECT * FROM welcome WHERE guildid = ?", (ctx.guild.id,))
        data = cursor.fetchone()
  
        if data:
          cursor.execute("UPDATE welcome SET channelid = ?, type = ?, message = ? WHERE guildid = ?", (channel.id, type, message, ctx.guild.id,))
          embed.description="Data succesfully updated!"
          
        else:
          cursor.execute("INSERT INTO welcome VALUES (?, ?, ?, ?)", (ctx.guild.id, channel.id, type, message,))
          embed.description="Data succesfully inserted!"
  
        conn.commit()
        conn.close()

      else:
        embed.title = "Error"
        embed.description = "You can't use this command. Missing permission 'Administrator'"

        
      await ctx.respond(embed=embed)
      
    #DEFAULT ROLE SETUP
    @setup.command(name="defaultrole", description=f"{cmdsdescription['defaultrolesetup']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def defaultrolesetup(self, ctx, role : Option(discord.Role, required=True)):
      embed = discord.Embed(
        title="Default Role Setup",
        color=discord.Colour.blue()
      )
      
      if ctx.author.guild_permissions.administrator: 
        
        conn = sqlite3.connect("kiwibot/database/welcome.db")
        cursor = conn.cursor()
  
        cursor.execute("SELECT * FROM defaultrole WHERE guildid = ?", (ctx.guild.id,))
        data = cursor.fetchone()
  
        if data:
          cursor.execute("UPDATE defaultrole SET channelid = ? WHERE guildid = ?", (role.id, ctx.guild.id,))
          embed.description="Data succesfully updated!"
          
        else:
          cursor.execute("INSERT INTO defaultrole VALUES (?, ?)", (ctx.guild.id, role.id,))
          embed.description="Data succesfully inserted!"
  
        conn.commit()
        conn.close()

      else:
        embed.title = "Error"
        embed.description = "You can't use this command. Missing permission 'Administrator'"

      await ctx.respond(embed=embed)
      
def setup(bot):
    bot.add_cog(Events(bot))
