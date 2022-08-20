import discord, math, json, random
from discord.ext import commands
from discord.commands import SlashCommandGroup 

class Nsfw(commands.Cog):
    def __init__(self, bot):
      self.bot = bot
      self.guildid = 1009052387324993538
      self.guild = None
      
      self.testid = 1009067480431476827
      self.boobsid = 1009052388423905383
      self.assid = 1009052982261858375
      self.asianid = 1009058797060374548
      self.pussyid = 1009058931483611186
      self.blowjobid = 1009541132633518253
      self.analid = 1009074649721737347
      
    nsfw = SlashCommandGroup("nsfw", "Commands related to nsfw")
  
    with open("kiwibot/json/description.json", "r") as dfile:
      cmdsdescription = json.load(dfile)
        
    @commands.Cog.listener()
    async def on_ready(self):
      self.guild = self.bot.get_guild(self.guildid)
      print("cmds.nsfw loaded")
      
    # NSFW COMMANDS #######################
      
    #PUSSY
    @nsfw.command(name="pussy", description=f"{cmdsdescription['nsfwpussy']}")
    @commands.is_nsfw()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def pussy(self, ctx):
      
      embed = discord.Embed(
        title=f"pussy",
        color = discord.Colour.red()
      )  
      
      all_messages = []
      correctChannel = None
      
      for guildChannel in self.guild.channels:
        if guildChannel.id == self.pussyid:
          correctChannel = guildChannel

      if correctChannel != None:
        async for message in correctChannel.history(limit = 100):
          all_messages.append(message)

        randomMessage = random.choice(all_messages)
        embed.set_image(url=randomMessage.attachments[0].url)

      else:
        embed.title = "Error"
        embed.description = "There was an error executing this command. Please try again later!"
      
      await ctx.respond(embed=embed)    

    #BOOBS
    @nsfw.command(name="boobs", description=f"{cmdsdescription['nsfwboobs']}")
    @commands.is_nsfw()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def boobs(self, ctx):
      
      embed = discord.Embed(
        title=f"boobs",
        color = discord.Colour.red()
      )  
      
      all_messages = []
      correctChannel = None
      
      for guildChannel in self.guild.channels:
        if guildChannel.id == self.boobsid:
          correctChannel = guildChannel

      if correctChannel != None:
        async for message in correctChannel.history(limit = 100):
          all_messages.append(message)

        randomMessage = random.choice(all_messages)
        embed.set_image(url=randomMessage.attachments[0].url)

      else:
        embed.title = "Error"
        embed.description = "There was an error executing this command. Please try again later!"
      
      await ctx.respond(embed=embed)   

    #ASS
    @nsfw.command(name="ass", description=f"{cmdsdescription['nsfwass']}")
    @commands.is_nsfw()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def ass(self, ctx):
      
      embed = discord.Embed(
        title=f"ass",
        color = discord.Colour.red()
      )  
      
      all_messages = []
      correctChannel = None
      
      for guildChannel in self.guild.channels:
        if guildChannel.id == self.assid:
          correctChannel = guildChannel

      if correctChannel != None:
        async for message in correctChannel.history(limit = 100):
          all_messages.append(message)

        randomMessage = random.choice(all_messages)
        embed.set_image(url=randomMessage.attachments[0].url)

      else:
        embed.title = "Error"
        embed.description = "There was an error executing this command. Please try again later!"
      
      await ctx.respond(embed=embed)   

    #ASIAN
    @nsfw.command(name="asian", description=f"{cmdsdescription['nsfwasian']}")
    @commands.is_nsfw()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def asian(self, ctx):
      
      embed = discord.Embed(
        title=f"asian",
        color = discord.Colour.red()
      )  
      
      all_messages = []
      correctChannel = None
      
      for guildChannel in self.guild.channels:
        if guildChannel.id == self.asianid:
          correctChannel = guildChannel

      if correctChannel != None:
        async for message in correctChannel.history(limit = 100):
          all_messages.append(message)

        randomMessage = random.choice(all_messages)
        embed.set_image(url=randomMessage.attachments[0].url)

      else:
        embed.title = "Error"
        embed.description = "There was an error executing this command. Please try again later!"
      
      await ctx.respond(embed=embed)   

    #BLOWJOB
    @nsfw.command(name="blowjob", description=f"{cmdsdescription['nsfwblowjob']}")
    @commands.is_nsfw()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def blowjob(self, ctx):
      
      embed = discord.Embed(
        title=f"blowjob",
        color = discord.Colour.red()
      )  
      
      all_messages = []
      correctChannel = None
      
      for guildChannel in self.guild.channels:
        if guildChannel.id == self.blowjobid:
          correctChannel = guildChannel

      if correctChannel != None:
        async for message in correctChannel.history(limit = 100):
          all_messages.append(message)

        randomMessage = random.choice(all_messages)
        embed.set_image(url=randomMessage.attachments[0].url)

      else:
        embed.title = "Error"
        embed.description = "There was an error executing this command. Please try again later!"
      
      await ctx.respond(embed=embed)   

    #ANAL
    @nsfw.command(name="anal", description=f"{cmdsdescription['nsfwanal']}")
    @commands.is_nsfw()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def anal(self, ctx):
      
      embed = discord.Embed(
        title=f"anal",
        color = discord.Colour.red()
      )  
      
      all_messages = []
      correctChannel = None
      
      for guildChannel in self.guild.channels:
        if guildChannel.id == self.analid:
          correctChannel = guildChannel

      if correctChannel != None:
        async for message in correctChannel.history(limit = 100):
          all_messages.append(message)

        randomMessage = random.choice(all_messages)
        embed.set_image(url=randomMessage.attachments[0].url)

      else:
        embed.title = "Error"
        embed.description = "There was an error executing this command. Please try again later!"
      
      await ctx.respond(embed=embed)   
  
def setup(bot):
    bot.add_cog(Nsfw(bot))
