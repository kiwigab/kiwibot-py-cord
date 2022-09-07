import discord, os, asyncpg, asyncio
from discord.ext import commands

bot = discord.Bot(debug_guilds=[1006631290012975218], intents=discord.Intents.all())
extension = discord.SlashCommandGroup("extension", "Commands related to extensions.")

# DATABASE ###################################
async def create_db_pool():
    bot.db = await asyncpg.create_pool(dsn="postgres://ronfyhjwgptcut:c9f7d021df9a617583dc002210442abf70628894dde92481a894e47781eba29b@ec2-52-30-75-37.eu-west-1.compute.amazonaws.com:5432/d6lbj76amrlnca")
    print("Succesfully connected to the database.")
    
# EVENTS ###################################

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
  
@bot.event
async def on_application_command_error(ctx, error):
  embed = discord.Embed(title="Error", description=error, color=discord.Colour.blue())
  await ctx.respond(embed=embed, delete_after=5)     
  
# EXTENSION COMMANDS ########################

#LOAD
@extension.command(guild_ids=[1006631290012975218], name="load", description="Load a specific extension")
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension("cogs." + extension)
    await ctx.respond("Loaded")

#UNLOAD
@extension.command(guild_ids=[1006631290012975218], name="unload", description="Unload a specific extension")
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension("cogs." + extension)
    await ctx.respond("Unloaded")
  
#RELOAD
@extension.command(guild_ids=[1006631290012975218], name="reload", description="Reload a specific extension")
@commands.is_owner()
async def reload(ctx, extension):
    bot.unload_extension("cogs." + extension)
    bot.load_extension("cogs." + extension)
    await ctx.respond("Reloaded")
  
for f in os.listdir("./kiwibot/cogs"):
  if f.endswith(".py"):
    bot.load_extension("cogs." + f[:-3])

bot.loop.run_until_complete(create_db_pool())
bot.add_application_command(extension)
bot.run('')