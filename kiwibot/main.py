import os, discord, sqlite3

from discord.ext import commands

bot = discord.Bot(debug_guilds=[1006631290012975218], intents=discord.Intents.all())
extension = discord.SlashCommandGroup("extension", "Commands related to extensions.")

# EVENTS ###################################

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
  
@bot.event
async def on_application_command_error(ctx, error):
  embed = discord.Embed(title="Error", description=error)
  await ctx.respond(embed=embed)     
  
# EXTENSION COMMANDS ########################

#LOAD
@extension.command(name="load", description="Load a specific extension")
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension("cogs." + extension)
    await ctx.respond("Loaded")

#UNLOAD
@extension.command(name="unload", description="Unload a specific extension")
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension("cogs." + extension)
    await ctx.respond("Unloaded")
  
#RELOAD
@extension.command(name="reload", description="Reload a specific extension")
@commands.is_owner()
async def reload(ctx, extension):
    bot.unload_extension("cogs." + extension)
    bot.load_extension("cogs." + extension)
    await ctx.respond("Reloaded")
  
for f in os.listdir("./kiwibot/cogs"):
  if f.endswith(".py"):
    bot.load_extension("cogs." + f[:-3])

bot.add_application_command(extension)
bot.run('OTc5NDc4NzkxMDExMzM2MjYy.GBaePa.AriQi1VK2oIogQrNSCdAVlLZK2m2YB_IrRTcB8')