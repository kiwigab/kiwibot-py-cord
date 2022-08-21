import discord, asyncio, json, humanfriendly, datetime

from discord import Option
from discord.commands import SlashCommandGroup, option
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    with open("kiwibot/json/description.json", "r") as dfile:
      cmdsdescription = json.load(dfile)
      
    role = SlashCommandGroup("role", "Commands related to roles")

    @commands.Cog.listener()
    async def on_ready(self):
      print("cmds.moderation loaded")

    # MODERATION COMMANDS #######################
    #REMOVE ROLE   
    @role.command(name="multiple", description=f"{cmdsdescription['multiplerole']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    @option(
      "filter",
      autocomplete=discord.utils.basic_autocomplete(["All", "Members", "Bots"]),
    )
  
    @option(
      "type",
      autocomplete=discord.utils.basic_autocomplete(["Give", "Remove"]),
    )
    async def multiplerole(self, ctx, member: discord.Member, role: discord.Role, filter : str, type : str):
                       
      embed = discord.Embed(title="Multiple Role", color=discord.Colour.blue())  
    
      if ctx.author.guild_permissions.manage_roles: 
        for member in ctx.guild.members:
          try:
            if filter == "All":
              if type == "Give":
                await member.add_roles(role)

              else:
                await member.remove_roles(role)

            elif filter == "Members":
              if type == "Give":
                if member.bot == False:
                  await member.add_roles(role)

              else:
                if member.bot == False:
                  await member.remove_roles(role)

            else:
              if type == "Give":
                if member.bot:
                  await member.add_roles(role)

              else:
                if member.bot:
                  await member.remove_roles(role)
              
          except:
            pass
            
      else:
        embed.title = "Error"
        embed.description = "You can't use this command. Missing permission 'Manage Roles'"
        
      await ctx.respond(embed=embed)
      
    #REMOVE ROLE   
    @role.command(name="remove", description=f"{cmdsdescription['removerole']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def removerole(self, ctx, member: discord.Member, role: discord.Role):
                       
      embed = discord.Embed(title="Remove Role", color=discord.Colour.blue(), description=f"❌Changed roles for {member.name}. Removed '{role.name}'!")  
    
      if ctx.author.guild_permissions.manage_roles: 
        try:
          if ctx.author.top_role > member.top_role:
            await member.remove_roles(role)
            
          else:
            embed.title = "Error"
            embed.description = f"{member.display_name} has a higher role in the hierarchy than you.."
              
        except:
          embed.title = "Error"
          embed.description = f"Something went wrong! {member.display_name} has a higher role in the hierarchy than me.."

      else:
        embed.title = "Error"
        embed.description = "You can't use this command. Missing permission 'Manage Roles'"
        
      await ctx.respond(embed=embed)
      
    #GIVE ROLE   
    @role.command(name="give", description=f"{cmdsdescription['giverole']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def giverole(self, ctx, member: discord.Member, role: discord.Role):
                       
      embed = discord.Embed(title="Give Role", color=discord.Colour.blue(), description=f"✅Changed roles for {member.name}. Added '{role.name}'!")  
    
      if ctx.author.guild_permissions.manage_roles: 
        try:
          if ctx.author.top_role > role:
            await member.add_roles(role)
            
          else:
            embed.title = "Error"
            embed.description = f"The role {role.name} is higher in the hierarchy than your role."
      
        except:
          embed.title = "Error"
          embed.description = "Something went wrong!"

      else:
        embed.title = "Error"
        embed.description = "You can't use this command. Missing permission 'Manage Roles'"
        
      await ctx.respond(embed=embed)
      

      
    #UNLOCK
    @commands.slash_command(name="unlock", description=f"{cmdsdescription['lock']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def unlock(self, ctx):
      embed = discord.Embed(title="Unlock", color=discord.Colour.blue(), description=f"{ctx.channel.mention} was unlocked. ✅")  
    
      if ctx.author.guild_permissions.manage_channels: 
        try:
          await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
      
        except:
          embed.title = "Error"
          embed.description = "Something went wrong! Can't unlock this channel.."

      else:
        embed.title = "Error"
        embed.description = "You can't use this command. Missing permission 'Manage Channels'"
        
      await ctx.respond(embed=embed)
      
    #LOCK
    @commands.slash_command(name="lock", description=f"{cmdsdescription['lock']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def lock(self, ctx):
      embed = discord.Embed(title="Lock", color=discord.Colour.blue(), description=f"{ctx.channel.mention} was locked. ❌")  
         
      if ctx.author.guild_permissions.manage_channels: 
        try:
          await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)  
      
        except:
          embed.title = "Error"
          embed.description = "Something went wrong! Can't lock this channel.."

      else:
        embed.title = "Error"
        embed.description = "You can't use this command. Missing permission 'Manage Channels'"
      
      await ctx.respond(embed=embed)
      
    #SOFTBAN
    @commands.slash_command(name="softban", description=f"{cmdsdescription['softban']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def softban(self, ctx, member : discord.Member):
      embed = discord.Embed(title="Softban", color=discord.Colour.blue(), description=f"{member.display_name}#{member.discriminator} was softbanned..")  
      
      if ctx.author.guild_permissions.ban_members:         
          try:      
            if ctx.author.top_role > member.top_role:        
              await member.ban()
              await asyncio.sleep(0.1)
              await ctx.guild.unban(member)  

            else:
              embed.title = "Error"
              embed.description = f"{member.display_name} has a higher role in the hierarchy than you.."
            
          except:
            embed.title = "Error"
            embed.description = "Something went wrong! You can't softban this member."

      else:
        embed.title = "Error"
        embed.description = "You can't use this command. Missing permission 'Ban Members'"
        
      await ctx.respond(embed=embed)

   #REMOVE TIMEOUT
    @commands.slash_command(name="removetimeout", description=f"{cmdsdescription['removetimeout']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def removetimeout(self, ctx, member : discord.Member):
      embed = discord.Embed(title="Timeout", color=discord.Colour.blue(), description=f"Removed timeout for {member.display_name}")  
    
      if ctx.author.guild_permissions.moderate_members:  
        try:
          if ctx.author.top_role > member.top_role:        
            await member.remove_timeout()

          else:
            embed.title = "Error"
            embed.description = f"{member.display_name} has a higher role in the hierarchy than you.."

        except:
          embed.title = "Error"
          embed.description = "Something went wrong! You can't remove the timeout for this member."

      else:
        embed.title = "Error"
        embed.description = "You can't use this command. Missing permission 'Timeout Members'"
      
      await ctx.respond(embed=embed)

      
   #TIMEOUT
    @commands.slash_command(name="timeout", description=f"{cmdsdescription['timeout']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def timeout(self, ctx, member : discord.Member, time, reason = None):
      embed = discord.Embed(title="Timeout", color=discord.Colour.blue(), description=f"{member.display_name} has been timed out.")  
    
      if ctx.author.guild_permissions.moderate_members:  
        try:
          if ctx.author.top_role > member.top_role:        
            time = humanfriendly.parse_timespan(time)
            await member.timeout(until=discord.utils.utcnow() + datetime.timedelta(seconds=time), reason=reason)

          else:
            embed.title = "Error"
            embed.description = f"{member.display_name} has a higher role in the hierarchy than you.."          

        except:
          embed.title = "Error"
          embed.description = "Something went wrong! You can't timeout this member."

      else:
        embed.title = "Error"
        embed.description = "You can't use this command. Missing permission 'Timeout Members'"
      
      await ctx.respond(embed=embed)
      
   #SETNICK
    @commands.slash_command(name="setnick", description=f"{cmdsdescription['setnick']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def setnick(self, ctx, member : discord.Member, nick):
      embed = discord.Embed(title="Setnick", color=discord.Colour.blue(), description=f"{member.name}'s nickname was set to {nick}'")  
      
      if ctx.author.guild_permissions.manage_nicknames:  
        try:
          if ctx.author.top_role > member.top_role:        
            await member.edit(nick=nick)

          else:
            embed.title = "Error"
            embed.description = f"{member.display_name} has a higher role in the hierarchy than you.."       


        except:
          embed.title = "Error"
          embed.description = "Something went wrong! You can't timeout this member."

      else:
        embed.title = "Error"
        embed.description = "You can't use this command. Missing permission 'Manage Nicknames'"
      
      await ctx.respond(embed=embed)

   #SLOWMODE
    @commands.slash_command(name="slowmode", description=f"{cmdsdescription['slowmode']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def slowmode(self, ctx, seconds: int):
      embed = discord.Embed(title="Slowmode", color=discord.Colour.blue(), description=f"Set the slowmode delay in this channel to {seconds} seconds!")  
      
      if ctx.author.guild_permissions.manage_channels:  
        try:
          await ctx.channel.edit(slowmode_delay=seconds)

        except:
          embed.title = "Error"
          embed.description = "Something went wrong! Can't modify slowmode delay.."

      else:
        embed.title = "Error"
        embed.description = "You can't use this command. Missing permission 'Manage Channels'"
      
      await ctx.respond(embed=embed)
      
   #CLEAR
    @commands.slash_command(name="clear", description=f"{cmdsdescription['clear']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def clear(self, ctx, 
                    amount : Option(int, min_value=0, max_value=500, required = True), 
                    member:  Option(discord.Member, required = False)
                                    
                    ):
      embed = discord.Embed(title="Clear", color=discord.Colour.blue(), description=f"Cleared {amount} messages sent by {member.name}.." if member else f"Cleared {amount} messages..")  
      def check(m):
        return m.author.id == member.id
        
      if ctx.author.guild_permissions.manage_messages:  
        try:
          if member:
            await ctx.channel.purge(check = check, limit = amount)

          else:
            await ctx.channel.purge(limit = amount)

        except:
          embed.title = "Error"
          embed.description = "Something went wrong!"
          
      else:
        embed.title = "Error"
        embed.description = "You can't use this command. Missing permission 'Manage Messages'"
      
      await ctx.respond(embed=embed, delete_after=5)
      
   #KICK
    @commands.slash_command(name="kick", description=f"{cmdsdescription['kick']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kick(self, ctx, member : discord.Member, reason = None):
      if ctx.author.guild_permissions.kick_members:         
        embed = discord.Embed(title="Kick", color=discord.Colour.blue(), description=f"{member.display_name}#{member.discriminator} was kicked!\nID: {member.id} \nReason: {reason}")  

        try:
          if ctx.author.top_role > member.top_role:        
            await member.kick(reason=reason)

          else:
            embed.title = "Error"
            embed.description = f"{member.display_name} has a higher role in the hierarchy than you.."       
          

        except:
          embed.title = "Error"
          embed.description = "Something went wrong! Can't kick this member."

      else:
        embed.title = "Error"
        embed.description = "You can't use this command. Missing permission 'Kick Members'"
      
      await ctx.respond(embed=embed)

   #BAN
    @commands.slash_command(name="ban", description=f"{cmdsdescription['ban']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ban(self, ctx, member : discord.Member, reason = None):
        embed = discord.Embed(title="Ban", color=discord.Colour.blue(), description=f"{member.display_name}#{member.discriminator} was banned..\nID: {member.id} \nReason: {reason}")  
        if ctx.author.guild_permissions.ban_members:     
 
          try:
            if ctx.author.top_role > member.top_role:        
              await member.ban(reason=reason)
  
            else:
              embed.title = "Error"
              embed.description = f"{member.display_name} has a higher role in the hierarchy than you.."   
  
          except:
            embed.title = "Error"
            embed.description = "Something went wrong! Can't ban this member."

        else:
          embed.title = "Error"
          embed.description = "You can't use this command. Missing permission 'Ban Members'"
          
        await ctx.respond(embed=embed)

    #UNBAN
    @commands.slash_command(name="unban", description=f"{cmdsdescription['unban']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def unban(self, ctx, user: discord.User):
        embed = discord.Embed(
          title="Unban",
          color=discord.Colour.blue(), 
        )
      
        if ctx.author.guild_permissions.ban_members:     
        
          try:
            banned = await ctx.guild.fetch_ban(user)
            embed.description = f"{banned.user.name} was unbanned!"
            await ctx.guild.unban(banned.user)
            
          except discord.NotFound:
            embed.title = "Error"
            embed.description = "Something went wrong! User was not found.."


        else:
          embed.title = "Error"
          embed.description = "You can't use this command. Missing permission 'Ban Members'"

        await ctx.respond(embed=embed)



    
def setup(bot):
    bot.add_cog(Moderation(bot))
