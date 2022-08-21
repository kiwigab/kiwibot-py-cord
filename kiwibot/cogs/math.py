import discord, math, json
from discord.ext import commands
from discord.commands import SlashCommandGroup 

class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    math = SlashCommandGroup("math", "Commands related to math")
  
    with open("kiwibot/json/description.json", "r") as dfile:
      cmdsdescription = json.load(dfile)
        
    @commands.Cog.listener()
    async def on_ready(self):
      print("cmds.math loaded")
      
    # MATH COMMANDS #####bguh##################
      
    #SQRT
    @math.command(name="sqrt", description=f"{cmdsdescription['sqrt']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def sqrt(self, ctx, number):
      sqrt = math.sqrt(int(number))
      
      embed = discord.Embed(
        title="Square Root",
        color = discord.Colour.blue(),
        description=f"sqrt({number}) = {sqrt}"
      )  
      
      await ctx.respond(embed=embed)    

   #POWER
    @math.command(name="power", description=f"{cmdsdescription['power']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def power(self, ctx, number, power):
      pow = math.pow(int(number), int(power))
      
      embed = discord.Embed(
        title="Power",
        color = discord.Colour.blue(),
        description=f"{number}^{power} = {pow}"
      )  
      
      await ctx.respond(embed=embed)   

   #SIN
    @math.command(name="sin", description=f"{cmdsdescription['sin']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def sin(self, ctx, number):
      sin = math.sin(int(number))
      
      embed = discord.Embed(
        title="Sin",
        color = discord.Colour.blue(),
        description=f"sin({number}) = {sin}"
      )  
      
      await ctx.respond(embed=embed)    
      
   #COS
    @math.command(name="cos", description=f"{cmdsdescription['cos']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def cos(self, ctx, number):
      cos = math.cos(int(number))
      
      embed = discord.Embed(
        title="Cos",
        color = discord.Colour.blue(),
        description=f"cos({number}) = {cos}"
      )  
      
      await ctx.respond(embed=embed)    

      
   #CALCULATOR 
    @math.command(name="calculator", description=f"{cmdsdescription['calculator']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def calculator(self, ctx, operation):
      embed = discord.Embed(
        title="Calculator",
        color = discord.Colour.blue(),
        description=f'{operation} = {eval(operation)}'
      )  
      
      await ctx.respond(embed=embed)    

   #AVERAGE
    @math.command(name="arithmeticmean", description=f"{cmdsdescription['arithmeticmean']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def arithmeticmean(self, ctx, numbers):

      list = numbers.split()
      nums = len(list)
     
      add = " + ".join(list)
      operation = f"({add}) / {nums}"
      
      embed = discord.Embed(
        title="Arithmetic Mean",
        color = discord.Colour.blue(),
        description=f'{operation} = {eval(operation)}'
      )  
      
      await ctx.respond(embed=embed)    

   #GEOMETRIC MEAN 
    @math.command(name="geometricmean", description=f"{cmdsdescription['geometricmean']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def geometricmean(self, ctx, numbers):

      list = numbers.split()
      nums = len(list)
     
      operation = " * ".join(list)
      result = eval(operation)
      
      embed = discord.Embed(
        title="Geometric Mean",
        color = discord.Colour.blue(),
        description=f'sqrt({operation}) = {math.sqrt(result)}'
      )  
      
      await ctx.respond(embed=embed)    

      
def setup(bot):
    bot.add_cog(Math(bot))
