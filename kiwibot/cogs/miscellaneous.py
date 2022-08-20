import discord, random, json, ipapi

from discord import Option
from datetime import datetime
from discord.ext import commands
from discord.commands import SlashCommandGroup 

class Miscellaneous(commands.Cog):
    def __init__(self, bot):
      self.bot = bot
      
      with open("kiwibot/json/colors.json", "r") as dfile:
        self.colours = json.load(dfile)

    with open("kiwibot/json/description.json", "r") as dfile:
      cmdsdescription = json.load(dfile)
          
    avatar = SlashCommandGroup("avatar", "Commands related to avatars")
    animals = SlashCommandGroup("animals", "Commands related to avatars")
  
    @commands.Cog.listener()
    async def on_ready(self):
      print("cmds.miscellaneous loaded")


    # ANIMALS COMMANDS #######################
      
    #DOG
    @animals.command(name="dog", description=f"{cmdsdescription['dog']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def dog(self, ctx):
        embed = discord.Embed(title="dog", color = discord.Colour.red())
      
        req = requests.get("https://some-random-api.ml/img/dog")
        data = req.json()

        embed.set_image(url=data["link"])
      
        await ctx.respond(embed=embed)   

    #CAT
    @animals.command(name="cat", description=f"{cmdsdescription['cat']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def cat(self, ctx):
        embed = discord.Embed(title="cat", color = discord.Colour.red())
      
        req = requests.get("https://some-random-api.ml/img/cat")
        data = req.json()

        embed.set_image(url=data["link"])
      
        await ctx.respond(embed=embed)    

    #FOX 
    @animals.command(name="fox", description=f"{cmdsdescription['fox']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def fox(self, ctx):
        embed = discord.Embed(title="fox", color = discord.Colour.red())
      
        req = requests.get("https://some-random-api.ml/img/fox")
        data = req.json()

        embed.set_image(url=data["link"])
      
        await ctx.respond(embed=embed)    

    #PANDA 
    @animals.command(name="panda", description=f"{cmdsdescription['panda']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def panda(self, ctx):
        embed = discord.Embed(title="panda", color = discord.Colour.red())
      
        req = requests.get("https://some-random-api.ml/img/panda")
        data = req.json()

        embed.set_image(url=data["link"])
      
        await ctx.respond(embed=embed)    

    #REDPANDA
    @animals.command(name="redpanda", description=f"{cmdsdescription['redpanda']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def redpanda(self, ctx):
        embed = discord.Embed(title="redpanda", color = discord.Colour.red())
      
        req = requests.get("https://some-random-api.ml/img/redpanda")
        data = req.json()

        embed.set_image(url=data["link"])
      
        await ctx.respond(embed=embed)    

    #KOALA
    @animals.command(name="koala", description=f"{cmdsdescription['koala']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def koala(self, ctx):
        embed = discord.Embed(title="koala", color = discord.Colour.red())
      
        req = requests.get("https://some-random-api.ml/img/koala")
        data = req.json()

        embed.set_image(url=data["link"])
      
        await ctx.respond(embed=embed)    

    #BIRD 
    @animals.command(name="bird", description=f"{cmdsdescription['bird']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def bird(self, ctx):
        embed = discord.Embed(title="koala", color = discord.Colour.red())
      
        req = requests.get("https://some-random-api.ml/img/bird")
        data = req.json()

        embed.set_image(url=data["link"])
      
        await ctx.respond(embed=embed)    

    #RACCOON
    @animals.command(name="raccoon", description=f"{cmdsdescription['raccoon']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def raccoon(self, ctx):
        embed = discord.Embed(title="koala", color = discord.Colour.red())
      
        req = requests.get("https://some-random-api.ml/img/koala")
        data = req.json()

        embed.set_image(url=data["link"])
      
        await ctx.respond(embed=embed)    

    #KANGAROO 
    @animals.command(name="kangaroo", description=f"{cmdsdescription['kangaroo']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kangaroo(self, ctx):
        embed = discord.Embed(title="kangaroo", color = discord.Colour.red())
      
        req = requests.get("https://some-random-api.ml/img/kangaroo")
        data = req.json()

        embed.set_image(url=data["link"])
      
        await ctx.respond(embed=embed)    

    # MISCELLANEOUS COMMANDS #######################
    
    #LOCATION
    @commands.slash_command(name="location", description=f"{cmdsdescription['geolocation']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def location(self, ctx, ip : str):
        embed = discord.Embed(
          title="GeoLocation",
          description=" ",
          color = discord.Colour.red()
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
          color = discord.Colour.red()
        )
      
        embed.add_field(name="Creator", value="kiwigab#4827", inline=False)
        embed.add_field(name="Version", value="0.6.9", inline=False)
        embed.add_field(name="Commands", value="Usage: /help <animals, fun, math, miscellaneous, moderation, nsfw>", inline=False)
    
        await ctx.respond(embed=embed)  
  
    #DM
    @commands.slash_command(name="dm", description=f"{cmdsdescription['dm']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def dm(self, ctx, message, member: discord.Member):
      word_list = message.split()
      embed = discord.Embed (
        title="Direct Message",
        color=discord.Colour.red(),
        description=f"Message: {message}\nAuthor: {ctx.author.name}"
      )
      
      try:
        if len(word_list) < 100:
          await member.send(message)
  
        else:
          embed.title = "Error"
          embed.description = "The message has too many words.."

      except:
          embed.title = "Error"
          embed.description = "This member has .."
      
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
        embed = discord.Embed(title="roll the dice", color=discord.Colour.red())
        embed.description = f"{rand}"
      
        await ctx.respond(embed=embed)       
      
   #CHOOSE
    @commands.slash_command(name="choose", description=f"{cmdsdescription['choose']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def choose(self, ctx, option1, option2):
        embed = discord.Embed(title="random chooser", color=discord.Colour.red())  
        list = [f"{option1}", f"{option2}"]     
        choice = random.choice(list)

        embed.description = f"{choice}"
        await ctx.respond(embed=embed)    
      
    #USER
    @commands.slash_command(name="user", description=f"{cmdsdescription['user']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def user(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        embed = discord.Embed(color=discord.Colour.red())
      
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
        embed = discord.Embed(color=discord.Colour.red(), title="Roles")
        result = ''
      
        for roles in ctx.guild.roles:
            result = result + '\n' + f'{roles.mention}'
            
        embed.description = result
        
        await ctx.respond(embed=embed)  
      
    #GUILD
    @commands.slash_command(name="guild", description=f"{cmdsdescription['guild']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def guild(self, ctx):
        embed = discord.Embed(color=discord.Colour.red())
        embed.set_author(name=f"{ctx.guild.name}", icon_url=f"{ctx.guild.icon.url}")

        guildId = ctx.guild.id
        embed.add_field(name="Guild ID:", value=f"{guildId}", inline=True)
      
        createdAt = ctx.guild.created_at.strftime('%Y-%m-%d')
        embed.add_field(name="Created at:", value=f"{createdAt}", inline=True)

        guildOwner = ctx.guild.owner.display_name
        embed.add_field(name="Owned by:", value=f"{guildOwner}", inline=True)     

        guildMemberCount = ctx.guild.member_count
        embed.add_field(name="Members:", value=f"{guildMemberCount}", inline=True)  
      
        textChannels = len(ctx.guild.text_channels)
        voiceChannels = len(ctx.guild.voice_channels)
        embed.add_field(name="Channels:", value=f"{textChannels} Text / {voiceChannels} Voice", inline=True)        

        rolesNumber = len(ctx.guild.roles)
        embed.add_field(name="Roles:", value=f"{rolesNumber}", inline=True)        
   
        await ctx.respond(embed=embed) 

    #USER AVATAR 
    @avatar.command(name="user", description=f"{cmdsdescription['useravatar']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def _user(self, ctx, user: discord.User = None):
        user = user or ctx.author

        embed = discord.Embed(title="user avatar",color=discord.Colour.red())
        embed.description = f"this avatar belongs to {user.display_name}"
        embed.set_image(url=f"{user.avatar.url}")

        await ctx.respond(embed=embed)  

    #MEMBER AVATAR
    @avatar.command(name="member", description=f"{cmdsdescription['memberavatar']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def _member(self, ctx, member: discord.Member = None):
        member = member or ctx.author

        embed = discord.Embed(title="member avatar",color=discord.Colour.red())
        embed.description = f"this avatar belongs to {member.display_name}"
        embed.set_image(url=f"{member.display_avatar.url}")

        await ctx.respond(embed=embed)  

    #GUILD AVATAR
    @avatar.command(name="guild", description=f"{cmdsdescription['guildavatar']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def _guild(self, ctx):
        embed = discord.Embed(title="guild avatar",color=discord.Colour.red())
        embed.set_image(url=f"{ctx.guild.icon.url}")

        await ctx.respond(embed=embed)   
      
def setup(bot):
    bot.add_cog(Miscellaneous(bot))
