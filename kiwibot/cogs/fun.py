import discord, random, requests, asyncio, os, textwrap, json

from bs4 import BeautifulSoup
from discord import Option
from discord.ext import commands
from discord.commands import SlashCommandGroup 
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from io import BytesIO
########################################
class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    with open("kiwibot/json/description.json", "r") as dfile:
      cmdsdescription = json.load(dfile)
      
    rate = SlashCommandGroup("rate", "Commands related to rates")
    text = SlashCommandGroup("text", "Commands related to text")
    img = SlashCommandGroup("image", "Commands related to images")
      
    @commands.Cog.listener()
    async def on_ready(self):
      print("cmds.fun loaded")
    # IMAGE COMMANDS #######################

    #WASTED
    @img.command(name="wasted", description=f"{cmdsdescription['wasted']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def wasted(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        wasted = Image.open("kiwibot/images/wasted.png")
        response = requests.get(member.display_avatar.url)
        avatar = Image.open(BytesIO(response.content))
        avatar = avatar.resize((256, 256))
        avatar = avatar.convert('L')
        canvas = Image.new("RGBA", (256, 256), (255, 255, 255, 0))
        canvas.paste(avatar, (0, 0), avatar)
        canvas.paste(wasted, (0, 0), wasted)
      
        
        wasted = wasted.convert("RGBA")

        canvas.save(f'wasted{member.name}.png')
     
        file=discord.File(f'wasted{member.name}.png')
      
        await ctx.respond(file=file)
        await asyncio.sleep(1)
        os.remove(f"wasted{member.name}.png")
      
    #SIMPCARD
    @img.command(name="simpcard", description=f"{cmdsdescription['simpcard']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def simpcard(self, ctx, member : discord.Member = None):
        member = member or ctx.author
      
        simpcard = Image.open("kiwibot/images/simpcard.png")
      
        response = requests.get(member.display_avatar.url)
      
        avatar = Image.open(BytesIO(response.content))
        avatar = avatar.resize((200, 240))
      
        simpcard.paste(avatar, (55, 110), avatar)

        textimg = ImageDraw.Draw(simpcard)
      
        font = ImageFont.truetype("kiwibot/fonts/Roboto-Light.ttf", 34)
        textimg.text((729/2, 420), f"{member.display_name}", font=font, anchor="mm", fill="#000")  
      
        simpcard.save(f'simpcard{member.name}.png')
      
        file=discord.File(f'simpcard{member.name}.png')
      
        await ctx.respond(file=file)
        await asyncio.sleep(1)
        os.remove(f"simpcard{member.name}.png")

      
    #GAY
    @img.command(name="gay", description=f"{cmdsdescription['gay']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def gay(self, ctx, member: discord.Member = None):
        member = member or ctx.author
      
        gay = Image.open("kiwibot/images/gay.png")
        gay =  gay.convert('RGB')
        gay.putalpha(140)
        gay = gay.resize((256, 256))
      
        response = requests.get(member.display_avatar.url)
      
        avatar = Image.open(BytesIO(response.content))
        avatar = avatar.resize((256, 256))
      
        avatar.paste(gay, (0, 0), gay)
        avatar.save(f'gay{member.name}.png')
      
        file=discord.File(f'gay{member.name}.png')
      
        await ctx.respond(file=file)
        await asyncio.sleep(1)
        os.remove(f"gay{member.name}.png")
      
    #POINTING
    @img.command(name="pointing", description=f"{cmdsdescription['pointing']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def pointing(self, ctx, member: discord.Member = None):
        member = member or ctx.author
      
        pointing = Image.open("kiwibot/images/pointing.png")
        pointing = pointing.resize((935, 698))
        pointing =  pointing.convert('RGB')
        response = requests.get(member.display_avatar.url)
      
        avatar = Image.open(BytesIO(response.content))
        avatar = avatar.resize((210, 210))
      
        pointing.paste(avatar, (300, 80), avatar)
        pointing.save(f'pointing{member.name}.png')
      
        file=discord.File(f'pointing{member.name}.png')
      
        await ctx.respond(file=file)
        await asyncio.sleep(1)
        os.remove(f"pointing{member.name}.png")
      
    #DREADS
    @img.command(name="dreads", description=f"{cmdsdescription['dreads']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def dreads(self, ctx, member: discord.Member = None):
        member = member or ctx.author
      
        dreads = Image.open("kiwibot/images/dreads.png")
        dreads = dreads.resize((378, 256))
        response = requests.get(member.display_avatar.url)
      
        avatar = Image.open(BytesIO(response.content))
        avatar = avatar.resize((256, 256))
      
        avatar.paste(dreads, (-65, -35), dreads)
        avatar.save(f'dreads{member.name}.png')
      
        file=discord.File(f'dreads{member.name}.png')
      
        await ctx.respond(file=file)
        await asyncio.sleep(1)
        os.remove(f"dreads{member.name}.png")

    #WIDE
    @img.command(name="wide", description=f"{cmdsdescription['wide']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def wide(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        response = requests.get(member.display_avatar.url)     
      
        wide = Image.open(BytesIO(response.content))
        wide = wide.resize((1012, 128))   
        wide.save(f'wide{member.name}.png')
        
        file=discord.File(f'wide{member.name}.png')
      
        await ctx.respond(file=file)
        await asyncio.sleep(1)

        os.remove(f"wide{member.name}.png")
    #ADULT CONTENT
    @img.command(name="adultcontent", description=f"{cmdsdescription['adultcontent']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def adultcontent(self, ctx, member: discord.Member = None):
        member = member or ctx.author
      
        adult18 = Image.open("kiwibot/images/18.png")
      
        response = requests.get(member.display_avatar.url)     
        adultcontent = Image.open(BytesIO(response.content))
        adultcontent = adultcontent.resize((256, 256))
        adult18 = adult18.resize((156, 156))
        adultcontent = adultcontent.filter(ImageFilter.BoxBlur(20))
        adultcontent.paste(adult18, (50 ,50), adult18)
      
        adultcontent.save(f'adultcontent{member.name}.png')
        
        file=discord.File(f'adultcontent{member.name}.png')
      
        await ctx.respond(file=file)
        await asyncio.sleep(1)
        os.remove(f"adultcontent{member.name}.png")

    #BLUR
    @img.command(name="blur", description=f"{cmdsdescription['blur']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def blur(self, ctx, member: discord.Member = None):
        member = member or ctx.author
      
        response = requests.get(member.display_avatar.url)     
        blur = Image.open(BytesIO(response.content))
        blur = blur.resize((256, 256))
        blur = blur.filter(ImageFilter.BoxBlur(5))
      
        blur.save(f'blur{member.name}.png')
      
        file=discord.File(f'blur{member.name}.png')
      
        await ctx.respond(file=file)
        await asyncio.sleep(1)
        os.remove(f"blur{member.name}.png")

    #FACTS
    @img.command(name="facts", description=f"{cmdsdescription['facts']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def facts(self, ctx, text):
        member = ctx.author
      
        facts = Image.open("kiwibot/images/facts.jpg")
        textimg = ImageDraw.Draw(facts)
      
        font = ImageFont.truetype("kiwibot/fonts/kindergarten.ttf", 25)
        textimg.text((35, 640), f"{textwrap.fill( text, 25 )}", fill=(0, 0, 0), font=font)  
      
        facts.save(f'facts{member.name}.png')
      
        file=discord.File(f'facts{member.name}.png')
      
        await ctx.respond(file=file)
        await asyncio.sleep(1)
        os.remove(f"facts{member.name}.png")

    #DELETE
    @img.command(name="delete", description=f"{cmdsdescription['delete']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def delete(self, ctx, member : discord.Member):
        member = member or ctx.author
      
        deletethis = Image.open("kiwibot/images/deletethis.png")
        response = requests.get(member.display_avatar.url)
      
        img = Image.open(BytesIO(response.content))
        img = img.resize((85, 85))
      
        deletethis.paste(img, (62 ,72), img)
        deletethis.save(f'delete{member.name}.png')
      
        file=discord.File(f'delete{member.name}.png')
      
        await ctx.respond(file=file)
        await asyncio.sleep(1)
        os.remove(f"delete{member.name}.png")

    #STRAWBERRIES
    @img.command(name="strawberries", description=f"{cmdsdescription['strawberries']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def strawberries(self, ctx, member : discord.Member):
        member = member or ctx.author
      
        strawberries = Image.open("kiwibot/images/strawberries.jpg")
        response = requests.get(member.display_avatar.url)
      
        img = Image.open(BytesIO(response.content))
        img = img.resize((250, 245))
      
        strawberries.paste(img, (200, 80), img)
        strawberries.save(f'strawberries{member.name}.png')
      
        file=discord.File(f'strawberries{member.name}.png')
      
        await ctx.respond(file=file)
        await asyncio.sleep(1)
        os.remove(f"strawberries{member.name}.png")
      
    #SLAP
    @img.command(name="slap", description=f"{cmdsdescription['slap']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def slap(self, ctx, member : discord.Member):
        slapimg = Image.open("kiwibot/images/slap.jpg")
        rresponse = requests.get(ctx.author.display_avatar.url)
        dresponse = requests.get(member.display_avatar.url)

        pfpr = Image.open(BytesIO(rresponse.content))
        pfpr = pfpr.resize((76, 75))
      
        pfpd = Image.open(BytesIO(dresponse.content))
        pfpd = pfpd.resize((76, 75))
      
        slapimg.paste(pfpr, (230, 30), pfpr)
        slapimg.paste(pfpd, (90, 20), pfpd)
      
        slapimg.save(f'slap{member.name}.png')
      
        file=discord.File(f'slap{member.name}.png')
      
        await ctx.respond(file=file)
        await asyncio.sleep(1)
        os.remove(f"slap{member.name}.png")
      
    #WANTED      
    @img.command(name="wanted", description=f"{cmdsdescription['wanted']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def wanted(self, ctx, member : discord.Member = None):
        member = member or ctx.author
      
        poster = Image.open("kiwibot/images/poster.jpg")
        response = requests.get(member.display_avatar.url)
      
        img = Image.open(BytesIO(response.content))
        img = img.resize((334, 329))
      
        poster.paste(img, (200, 285), img)
        poster.save(f'wanted{member.name}.png')
      
        file=discord.File(f'wanted{member.name}.png')
      
        await ctx.respond(file=file)
        await asyncio.sleep(1)
        os.remove(f"wanted{member.name}.png")

      
    # TEXT COMMANDS #######################

    #EMOJIFY
    @text.command(name="emojify", description=f"{cmdsdescription['emojify']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def emojify(self, ctx, text):
        emojis = []
        for s in text.lower():
          if s.isdecimal():
            numbers = { 
              '1' : 'one', 
              '2' : 'two',
              '3' : 'three',
              '4' : 'four',
              '5' : 'five',
              '6' : 'six',
              '7' : 'seven',
              '8' : 'eight',
              '9' : 'nine'
            }
            emojis.append(f':{numbers.get(s)}:')
            
          elif s.isalpha():
            emojis.append(f':regional_indicator_{s}:')

          else:
            emojis.append(s)
            
        await ctx.respond(''.join(emojis)) 

    #SPOILER 
    @text.command(name="spoiler", description=f"{cmdsdescription['spoiler']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def spoiler(self, ctx, text): 
        result = ''    
        for character in text:
          if character != " ":
            result += "||  " + character + "  ||"
                  
        await ctx.respond(result) 
      
    #TRUMPET 
    @text.command(name="trumpet", description=f"{cmdsdescription['trumpet']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def trumpet(self, ctx, text):
        separator = "🎺"
        result = ''
        for character in text:
          if character != " ":
            result = result + separator + character
            
        result += separator    
        await ctx.respond(result) 

    #CAPITALIZE 
    @text.command(name="capitalize", description=f"{cmdsdescription['capitalize']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def capitalize(self, ctx, text):
        separator = " "
        result = ''
        for character in text:
          if character != " ":
            result = result + separator + character.capitalize()
            
        result += separator    
        await ctx.respond("**" + result + "**") 
      
    #SKULL 
    @text.command(name="skull", description=f"{cmdsdescription['skull']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def skull(self, ctx, text):
        separator = "💀"
        result = ''
        for character in text:
          if character != " ":
            result = result + separator + character
            
        result += separator    
        await ctx.respond(result) 
      
    #CLAP 
    @text.command(name="clap", description=f"{cmdsdescription['clap']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def clap(self, ctx, text):
        separator = "👏"
        result = ''
        for character in text:
          if character != " ":
            result = result + separator + character
            
        result += separator    
        await ctx.respond(result) 

    # RATE COMMANDS #######################
     
    #EPIC GAMER
    @rate.command(name="epicgamer", description=f"{cmdsdescription['epicgamerrate']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def epicgamerrate(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        rand = random.randint(0, 100)

        embed = discord.Embed(title="epic gamer rate machine never lies",color=discord.Colour.red())
        
        if rand >= 30:
          embed.description = f"{member.display_name} este {rand}% gamer"

        if rand < 30:
          embed.description = f"{member.display_name} este {rand}% gamer"
          
        await ctx.respond(embed=embed) 
      
    #THOT
    @rate.command(name="thot", description=f"{cmdsdescription['thotrate']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def thotrate(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        rand = random.randint(0, 100)

        embed = discord.Embed(title="thot rate machine never lies",color=discord.Colour.red())
        
        if rand >= 30:
          embed.description = f"{member.display_name} este {rand}% thotty"

        if rand < 30:
          embed.description = f"{member.display_name} este {rand}% thotty"
          
        await ctx.respond(embed=embed) 
      
    #GAY
    @rate.command(name="gay", description=f"{cmdsdescription['gayrate']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def gayrate(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        rand = random.randint(0, 100)

        embed = discord.Embed(title="gay rate machine never lies",color=discord.Colour.red())
        
        if rand >= 30:
          embed.description = f"{member.display_name} este {rand}% gay🏳️‍🌈"
          embed.color = discord.Colour.magenta()

        if rand < 30:
          embed.description = f"{member.display_name} este {rand}% gay📏"
          embed.color = discord.Colour.blue()  
          
        await ctx.respond(embed=embed) 
      
    #SIMP
    @rate.command(name="simp", description=f"{cmdsdescription['simprate']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def simprate(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        rand = random.randint(1, 30)

        embed = discord.Embed(title="simp rate machine never lies",color=discord.Colour.red())
        
        if rand >= 30:
          embed.description = f"{member.display_name} este {rand}% simp.. Sunt dezamagit de el"
          
        if rand < 30:
          embed.description = f"{member.display_name} este {rand}% simp.. Foarte bine soldat"

        await ctx.respond(embed=embed) 
      
    #STANK
    @rate.command(name="stank", description=f"{cmdsdescription['stankrate']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def stankrate(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        rand = random.randint(1, 30)

        embed = discord.Embed(title="stank rate machine never lies",color=discord.Colour.red())
        
        if rand >= 30:
          embed.description = f"{member.display_name} este {rand}% stanky.. Spala-te bine la organul genital masculin de reproducere jegosule."
          
        if rand < 30:
          embed.description = f"{member.display_name} este {rand}% simp.. TE SPELI?"

        await ctx.respond(embed=embed) 
      
    #TERMINAT
    @rate.command(guild_ids=[937419314968019004], name="terminat", description=f"{cmdsdescription['terminatrate']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def termiantrate(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        rand = random.randint(0, 100)

        embed = discord.Embed(title="termiant rate machine never lies",color=discord.Colour.red())
        
        if rand >= 30:
          embed.description = f"{member.display_name} este {rand}% terminat.. Sunt mandru de el"

        if rand < 39:
          embed.description = f"{member.display_name} este {rand}% terminat.. Un ratat"
          
        await ctx.respond(embed=embed) 

    # FUN COMMANDS #######################
      
    #STAPINESCU
    @commands.slash_command(name="dadjoke", description=f"{cmdsdescription['dadjoke']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def dadjoke(self, ctx):
        embed = discord.Embed(
          title="just a dad joke",
          color = discord.Colour.red()
        )
      
        page = requests.get("https://icanhazdadjoke.com/")
        soup = BeautifulSoup(page.text, 'html5lib')
        dadjoke = soup.find('div', {"class": "card-content"})

        embed.description = f"{dadjoke.text}"
      
        await ctx.respond(embed=embed)  
      
    #STAPINESCU
    @commands.slash_command(name="stapinescu", description=f"{cmdsdescription['stapinescu']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def stapinescu(self, ctx):
        embed = discord.Embed(
          title="cuvinte celebre spuse de stapinu",
          color = discord.Colour.red()
        )
      
        rand = random.randint(0, 153)
        url = f"https://stapinescu.com/cuvinte-memorabile-{rand}"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html5lib')
        stapinul = soup.find('div', {"class": "card-body text-center"})

        embed.description = f"{stapinul.text}"
      
        await ctx.respond(embed=embed)   
  
    #ROAST 
    @commands.slash_command(name="roast", description=f"{cmdsdescription['roast']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def roast(self, ctx, member : discord.Member = None):
        member = member or ctx.author
        embed = discord.Embed(title="roast", color = discord.Colour.red())
      
        page = requests.get(f"https://insult.mattbas.org/api/insult.html?who={member.display_name}")
        soup = BeautifulSoup(page.text, 'html5lib')
        insult = soup.find('h1', {"class": "insult"})

        embed.description = f"{insult.text}"
      
        await ctx.respond(embed=embed)   

    #MEME
    @commands.slash_command(name="meme", description=f"{cmdsdescription['meme']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def meme(self, ctx):
        embed = discord.Embed(title="meme", color = discord.Colour.red())
      
        req = requests.get("https://some-random-api.ml/meme")
        data = req.json()

        embed.set_image(url=data["image"])
      
        await ctx.respond(embed=embed)   
      
    #8BALL 
    @commands.slash_command(name="8ball", description=f"{cmdsdescription['8ball']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def _8ball(self, ctx, question):
        embed = discord.Embed(title="8ball", color=discord.Colour.red())
      
        list = [
          'DA ESTI TERMINAT?',
          'ESTI TERMINAT? N-AM DE UNDE SA STIU NU SUNT AKINATOR..',
          'PROBABIL..', 
          'SUNT TERMINAT SI NU STIU SIGUR',
          'NU, TERMINATULE', 
          'ESTI TERMINAT?', 
          'AI DAT RELOAD?',
          'INTREBAREA ASTA NU ARE NICIUN SENS TERMINATULE..',
        ]
      
        answer = random.choice(list)
        embed.add_field(name="Question",value=f'{question}',inline=False)
        embed.add_field(name="Answer",value=f'{answer}',inline=False)
      
        await ctx.respond(embed=embed) 

    #HACK
    @commands.slash_command(name="hack", description=f"{cmdsdescription['hack']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def hack(self, ctx, member : discord.Member):
        ctx.defer()
        member = member or ctx.author
        message = await ctx.send(f"HACKING {member.display_name}")
        await asyncio.sleep(2)
        await message.edit(content="Stealing password and email from discord..")

        await asyncio.sleep(3)
        await message.edit(content=f"Email: {member.display_name}@ilikepp.com \nPassword: iamgay#@andilovehaur")
        
        await asyncio.sleep(3)
        await message.edit(content=f"Fetching last private message..")

        await asyncio.sleep(3)
        await message.edit(content=f"Message: let's meet i want big salami \nAuthor: {member.mention}")

        await asyncio.sleep(3)
        await message.edit(content=f"!!!HACKING EPIC GAMES ACCOUNT!!!")

        await asyncio.sleep(3)
        await message.edit(content=f"Email: {member.display_name}@ilikefn.com \nPassword: ILOVEFORTNITE")

        await asyncio.sleep(3)
        await message.edit(content=f"DELETING EPIC GAMES ACCOUNT.. NO MORE FORTNITE")
   
        await asyncio.sleep(3)
        await message.edit(content=f"!!{member.display_name} hacked succesfully!!")
      
    
    #PUSSY 
    @commands.slash_command(name="pussy", description=f"{cmdsdescription['pussy']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def pussy(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        list = ['{}', '[{}]', '()', '[]', '({})', '{]', '[}']
        choice = random.choice(list)
      
        embed = discord.Embed(title="pussy machine never lies", description=f"organul genital feminin de reproducere al lui {member.name} arata asa: \n{choice}", color=discord.Colour.red())
        await ctx.respond(embed=embed) 
      
    #PENIS
    @commands.slash_command(name="penis", description=f"{cmdsdescription['penis']}")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def penis(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        rand = random.randint(1, 30)
        lenght = "=" * rand
      
        embed = discord.Embed(
          title="penis machine never lies",
          description = f"{member.display_name}'s penis \n8{lenght}>",
          color=discord.Colour.red()
        )
      
        await ctx.respond(embed=embed) 


      
def setup(bot):
    bot.add_cog(Fun(bot))
