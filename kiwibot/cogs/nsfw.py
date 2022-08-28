import discord, json, random
from discord.ext import commands
from discord.commands import option 

class Nsfw(commands.Cog):
    def __init__(self, bot):
      self.bot = bot
      self.guildid = 1009052387324993538
      self.guild = None
      
      self.nsfwid = {
        "test" : 1009067480431476827,
        "boobs" : 1009052388423905383,
        "ass" : 1009052982261858375,
        "asian" : 1009058797060374548,
        "pussy" : 1009058931483611186,
        "blowjob" : 1009541132633518253,
        "anal" : 1009074649721737347
      }
      
    with open("kiwibot/json/description.json", "r") as dfile:
      cmdsdescription = json.load(dfile)
        
    @commands.Cog.listener()
    async def on_ready(self):
      self.guild = self.bot.get_guild(self.guildid)
      print("cmds.nsfw loaded")
      
    # NSFW COMMANDS #######################
      
    #PUSSY
    @commands.slash_command(name="nsfw", description=f"{cmdsdescription['nsfw']}")
    @commands.cooldown(1, 15, commands.BucketType.user)
    @option(
      "type",
      autocomplete=discord.utils.basic_autocomplete(["pussy", "ass", "anal", "asian", "boobs", "blowjob"]),
    )
    async def nsfw(self, ctx, type : str):
      
      embed = discord.Embed(
        title=f"{type}",
        color = discord.Colour.blue()
      )  
      
      all_messages = []
      correctChannel = None
      
      for guildChannel in self.guild.channels:
        if guildChannel.id == self.nsfwid[type]:
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
