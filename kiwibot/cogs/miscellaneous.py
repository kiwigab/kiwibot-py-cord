import discord, random, json, ipapi, requests

from discord import Option
from datetime import datetime
from discord.ext import commands
from discord.commands import SlashCommandGroup, option

class Miscellaneous(commands.Cog):
    def __init__(self, bot):
      self.bot = bot
      
      with open("kiwibot/json/colors.json", "r") as dfile:
        self.colours = json.load(dfile)

    with open("kiwibot/json/description.json", "r") as dfile:
      cmdsdescription = json.load(dfile)
          
    @commands.Cog.listener()
    async def on_ready(self):
      print("cmds.miscellaneous loaded")

    # MISCELLANEOUS COMMANDS #######################

    #ANIMALS
    @commands.slash_command(name="animals", description=f"{cmdsdescription['animals']}")
    @commands.cooldown(1, 10, commands.BucketType.user)
    @option(
      "type",
      autocomplete=discord.utils.basic_autocomplete(["dog", "cat", "fox", "panda", "redpanda", "koala", "bird", "raccoon", "kangaroo"]),
    )
    async def animals(self, ctx, type : str):  
        embed = discord.Embed(
          title=f"{type}",
          color=discord.Colour.blue())   

        if type == "redpanda":
          data = requests.get(f"https://some-random-api.ml/img/red_panda").json()

        else:
          data = requests.get(f"https://some-random-api.ml/img/{type}").json()
        
        embed.set_image(url=data["link"])        
        await ctx.respond(embed=embed)

    #AVATAR
    @commands.slash_command(name="avatar", description=f"{cmdsdescription['avatar']}")
    @commands.cooldown(1, 10, commands.BucketType.user)
    @option(
      "type",
      autocomplete=discord.utils.basic_autocomplete(["user_discord", "user_guild", "guild"]),
    )
    async def avatar(self, ctx, type : str, user : discord.Member = None):  
        embed = discord.Embed(
          title="user avatar",
          description = f"this avatar belongs to {user.display_name}",
          color=discord.Colour.blue()
        )
        if user and type != "guild":
          if type == "user_discord":
            embed.set_image(url=f"{user.avatar.url}")

          if type == "user_guild":
            embed.set_image(url=f"{user.display_avatar.url}")
        
        else:
          embed.title = "Error"
          embed.description = "Option 'user' is empty."
        
        if type == "guild":
          embed.title = "guild avatar"
          embed.description = " "
          embed.set_image(url=f"{ctx.guild.icon.url}")

        await ctx.respond(embed=embed)  

    #LOCATION
    @commands.slash_command(name="location", description=f"{cmdsdescription['geolocation']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def location(self, ctx, ip : str):
        embed = discord.Embed(
          title="GeoLocation",
          description=" ",
          color = discord.Colour.blue()
        )
      
        data = ipapi.location(ip = ip, output='json')

        embed.add_field(name="IP", value=f"{data['ip']}", inline=True)
        embed.add_field(name="City", value=f"{data['city']}", inline=True)
        embed.add_field(name="Region", value=f"{data['region']}", inline=True)
        embed.add_field(name="Region Code", value=f"{data['region_code']}", inline=True)
        embed.add_field(name="Country", value=f"{data['country']}", inline=True)
        embed.add_field(name="County Code", value=f"{data['country_code']}", inline=True)
        embed.add_field(name="Country Capital", value=f"{data['country_capital']}", inline=True)
        embed.add_field(name="Country TLD", value=f"{data['country_tld']}", inline=True)
        embed.add_field(name="Country Name", value=f"{data['country_name']}", inline=True)
        embed.add_field(name="Continent Code", value=f"{data['continent_code']}", inline=True)
        embed.add_field(name="IN EU", value=f"{data['in_eu']}", inline=True)
        embed.add_field(name="Latitude & Longitude", value=f"{data['latitude']} {data['longitude']}", inline=True)
        embed.add_field(name="Time Zone", value=f"{data['timezone']}", inline=True)
        embed.add_field(name="UTC Offset", value=f"{data['utc_offset']}", inline=True)
        embed.add_field(name="Country Calling Code", value=f"{data['country_calling_code']}", inline=True)
        embed.add_field(name="Currency", value=f"{data['currency']}", inline=True)
        embed.add_field(name="Currency Name", value=f"{data['currency_name']}", inline=True)
        embed.add_field(name="Languages", value=f"{data['languages']}", inline=True)
        embed.add_field(name="Country Area", value=f"{data['country_area']}", inline=True)
        embed.add_field(name="Country Population", value=f"{data['country_population']}", inline=True)
        embed.add_field(name="ASN", value=f"{data['asn']}", inline=True)
        embed.add_field(name="ORG", value=f"{data['org']}", inline=True)

        await ctx.author.send(embed=embed)
        await ctx.respond("ip details sent to pm")  

    #PING
    @commands.slash_command(name="ping", description=f"{cmdsdescription['ping']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ping(self, ctx):
        await ctx.respond(f'Pong! In {round(self.bot.latency * 1000)}ms')  
      
   #CREATE EMBED
    @commands.slash_command(name="embed", description=f"{cmdsdescription['embed']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.has_permissions(manage_messages=True)
    async def createembed(self, ctx,
                          title : Option(str, description="The title of the embed..", required=True),
                          description : Option(str, description="The description of the embed..", required=True),
                          colour : Option(str, description="The colour of the embed..", required=False),
                          image : Option(str, description="The url of an image for the embed..", required=False),
                          author : Option(discord.Member, description="The author of the embed..", required=False),
                          footer : Option(str, description="The footer of the embed..", required=False),
                          thumbnail : Option(str, description="The thumbnail of the embed..", required=False)                          
                        ):

        embed = discord.Embed()
                          
        if title:
          embed.title = f"{title}"

        if description:
          embed.description = f"{description}"

        if colour:
          embed.color = eval(self.colours[colour])

        if image:
          embed.set_image(url=image)

        if author:
          embed.set_author(name=author.name, icon_url=author.avatar.url)

        if footer:
          embed.set_footer(text=footer)

        if thumbnail:
          embed.set_thumbnail(url=thumbnail)
          
        await ctx.respond("Embed was created succesfully!")   
        await ctx.send(embed=embed)   
        
   #NICK
    @commands.slash_command(name="nick", description=f"{cmdsdescription['nick']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.has_permissions(manage_messages=True)
    async def nick(self, ctx, nick):
      if ctx.author.guild_permissions.change_nickname:  
        await ctx.author.edit(nick=nick)
        await ctx.respond(f"{ctx.author.name}, your name was sucessfully changed to {nick}", delete_after=2)   
        
    # HELP
    @commands.slash_command(name="help", description=f"{cmdsdescription['help']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def help(self, ctx, command: str = None):
        embed = discord.Embed(
          title="Help",
          description=" ",
          color = discord.Colour.blue()
        )
      
        embed.add_field(name="Creator", value="kiwigab#4827", inline=False)
        embed.add_field(name="Version", value="0.6.9", inline=False)

        await ctx.respond(embed=embed)  
  
    #DM
    @commands.slash_command(name="dm", description=f"{cmdsdescription['dm']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def dm(self, ctx, message, member: discord.Member):
      word_list = message.split()
      embed = discord.Embed (
        title="Direct Message",
        color=discord.Colour.blue(),
        description=f"Message: {message}\nAuthor: {ctx.author.name}"
      )
      
      try:
        await member.send(message)

      except:
        embed.title = "Error"
        embed.description = "Someting went wrong. Can't send a message to this member!"
      
    #SAY
    @commands.slash_command(name="say", description=f"{cmdsdescription['say']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def say(self, ctx, text):
        await ctx.respond(text)     
      
    #ROLL
    @commands.slash_command(name="roll", description=f"{cmdsdescription['roll']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def roll(self, ctx, number):
        rand = random.randint(0, int(number))     
        embed = discord.Embed(title="roll the dice", color=discord.Colour.blue())
        embed.description = f"{rand}"
      
        await ctx.respond(embed=embed)       
      
   #CHOOSE
    @commands.slash_command(name="choose", description=f"{cmdsdescription['choose']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def choose(self, ctx, option1, option2):
        embed = discord.Embed(title="random chooser", color=discord.Colour.blue())  
        choice = random.choice([f"{option1}", f"{option2}"] )

        embed.add_field(name="Options:", value=f"1: {option1}\n2: {option2}", inline=False)
        embed.add_field(name="Chosen:", value=f"{choice}", inline=False)
        await ctx.respond(embed=embed)    
      
    #USER
    @commands.slash_command(name="user", description=f"{cmdsdescription['user']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def user(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        embed = discord.Embed(color=discord.Colour.blue())
      
        joinedserver = member.joined_at.strftime('%Y-%m-%d')
        embed.add_field(name="Joined server:", value=f"{joinedserver}", inline=True)    
      
        joineddiscord = member.created_at.strftime('%Y-%m-%d')
        embed.add_field(name="Joined discord:", value=f"{joineddiscord}", inline=True)    

        embed.set_author(name="User, " + member.display_name, icon_url=member.avatar.url)
      
        await ctx.respond(embed=embed)  

    #ROLES
    @commands.slash_command(name="roles", description=f"{cmdsdescription['roles']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def roles(self, ctx):
        embed = discord.Embed(color=discord.Colour.blue(), title="Roles")
        result = ''
      
        for roles in ctx.guild.roles:
            result = result + '\n' + f'{roles.mention}'
            
        embed.description = result
        
        await ctx.respond(embed=embed)  
      
    #GUILD
    @commands.slash_command(name="guild", description=f"{cmdsdescription['guild']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def guild(self, ctx):
        embed = discord.Embed(color=discord.Colour.blue())
        embed.set_author(name=f"{ctx.guild.name}", icon_url=f"{ctx.guild.icon.url}")

        guildId = ctx.guild.id
        embed.add_field(name="🆔Guild ID:", value=f"{guildId}", inline=True)
      
        createdAt = ctx.guild.created_at.strftime('%Y-%m-%d')
        embed.add_field(name="⏰Created at:", value=f"{createdAt}", inline=True)

        guildOwner = ctx.guild.owner.display_name
        embed.add_field(name="👑Owned by:", value=f"{guildOwner}", inline=True)     

        guildMemberCount = ctx.guild.member_count
        embed.add_field(name="😃Members:", value=f"{guildMemberCount}", inline=True)  
      
        textChannels = len(ctx.guild.text_channels)
        voiceChannels = len(ctx.guild.voice_channels)
        embed.add_field(name="📺Channels:", value=f"{textChannels} Text / {voiceChannels} Voice", inline=True)        

        rolesNumber = len(ctx.guild.roles)
        embed.add_field(name="👮Roles:", value=f"{rolesNumber}", inline=True)        
   
        await ctx.respond(embed=embed) 
      
def setup(bot):
    bot.add_cog(Miscellaneous(bot))
