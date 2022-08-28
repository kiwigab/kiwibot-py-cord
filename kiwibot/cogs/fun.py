import discord, random, requests, asyncio, os, textwrap, json, unidecode

from bs4 import BeautifulSoup
from discord.ext import commands
from discord.commands import option
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops, ImageOps
from io import BytesIO

class Fun(commands.Cog):
    def __init__(self, bot):
      self.bot = bot

    with open("kiwibot/json/description.json", "r") as dfile:
      cmdsdescription = json.load(dfile)
      
    @commands.Cog.listener()
    async def on_ready(self):
      print("cmds.fun loaded")

    # FUN COMMANDS #######################

    #IMAGE
    @commands.slash_command(name="image", description=f"{cmdsdescription['image']}")
    @commands.cooldown(1, 10, commands.BucketType.user)
    @option(
      "type",
      autocomplete=discord.utils.basic_autocomplete(["delete", "jail", "invert", "fedora", "gravestone", "dreads", "facts", "gay", "pointing", "wide", "blur", "wasted", "simpcard", "slap", "wanted", "egg"]),
    )
    async def image(self, ctx, type : str, text : str = None, user1 : discord.Member = None, user2 : discord.Member = None):
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

      user = user1 or ctx.author
      user1_avatar = Image.open(BytesIO(requests.get(user.display_avatar.url).content))
      user2_avatar = Image.open(BytesIO(requests.get(user2.display_avatar.url).content)) if user2 else None
      embed = discord.Embed(title="Error", description="Something went wrong. Please try again later!", color=discord.Colour.blue())

      if type == "delete":
        imageDelete = Image.open("kiwibot/images/delete.png")
        user1_avatar = user1_avatar.resize((85, 85))
        imageDelete.paste(user1_avatar, (62 ,72), user1_avatar)
        imageDelete.save(f'{type}{user.name}.png')
      
      if type == "dreads":
        imageDreads = Image.open("kiwibot/images/dreads.png")
        imageDreads = imageDreads.resize((378, 256))
        user1_avatar = user1_avatar.resize((256, 256))
        user1_avatar.paste(imageDreads, (-65, -35), imageDreads)
        user1_avatar.save(f'{type}{user.name}.png')

      if type == "facts":
        if text != None:
          imageFacts = Image.open("kiwibot/images/facts.jpg")
          textOnImage = ImageDraw.Draw(imageFacts)
          font = ImageFont.truetype("kiwibot/fonts/Roboto-Light.ttf", 20)
          textWarp = textwrap.fill(unidecode.unidecode(text), 25)
          textOnImage.text((35, 640), f"{textWarp}", fill=(0, 0, 0), font=font)  
          imageFacts.save(f'{type}{user.name}.png')

        else:
          embed.description = "The option 'text' is empty."

      if type == "gay":
        imageGay = Image.open("kiwibot/images/gay.png").convert('RGB')
        imageGay = imageGay.resize((256, 256))
        imageGay.putalpha(140)

        user1_avatar = user1_avatar.resize((256, 256))
        user1_avatar.paste(imageGay, (0, 0), imageGay)
        user1_avatar.save(f'{type}{user.name}.png')     

      if type == "pointing":
        imagePointing = Image.open("kiwibot/images/pointing.png").convert('RGB')
        imagePointing = imagePointing.resize((935, 698))
        user1_avatar = user1_avatar.resize((210, 210))
        imagePointing.paste(user1_avatar, (300, 80), user1_avatar)
        imagePointing.save(f'{type}{user.name}.png')

      if type == "wide":
        user1_avatar = user1_avatar.resize((512, 128))   
        user1_avatar.save(f'{type}{user.name}.png')

      if type == "blur":
        user1_avatar = user1_avatar.resize((256, 256))
        user1_avatar = user1_avatar.filter(ImageFilter.BoxBlur(5))
        user1_avatar.save(f'{type}{user.name}.png')
        
      if type == "wasted":
        imageWasted = Image.open("kiwibot/images/wasted.png").convert("RGBA")
        user1_avatar = user1_avatar.resize((256, 256))
        user1_avatar = user1_avatar.convert('L')
        wastedCanvas = Image.new("RGBA", (256, 256), (255, 255, 255, 0))
        wastedCanvas.paste(user1_avatar, (0, 0), user1_avatar)
        wastedCanvas.paste(imageWasted, (0, 0), imageWasted)
        wastedCanvas.save(f'{type}{user.name}.png')

      if type == "simpcard":
        imageSimpcard = Image.open("kiwibot/images/simpcard.png")
        user1_avatar = user1_avatar.resize((200, 240))
        imageSimpcard.paste(user1_avatar, (55, 110), user1_avatar)
        textOnImage = ImageDraw.Draw(imageSimpcard)
        font = ImageFont.truetype("kiwibot/fonts/Roboto-Light.ttf", 33)
        textOnImage.text((729/2, 420), f"{user.display_name}", font=font, anchor="mm", fill="#000")  
        imageSimpcard.save(f'{type}{user.name}.png')

      if type == "slap":
        if user2 != None:
          imageSlap = Image.open("kiwibot/images/slap.jpg")
          user1_avatar = user1_avatar.resize((76, 75))
          user2_avatar = user2_avatar.resize((76, 75))
          imageSlap.paste(user1_avatar, (230, 30), user1_avatar)
          imageSlap.paste(user2_avatar, (90, 20), user2_avatar)
          imageSlap.save(f'{type}{user.name}.png')

        else:
          embed.description = "The option 'user2' is empty."
      
      if type == "wanted":
        imageWanted = Image.open("kiwibot/images/wanted.jpg")
        user1_avatar = user1_avatar.resize((334, 329))
        imageWanted.paste(user1_avatar, (200, 285), user1_avatar)
        imageWanted.save(f'{type}{user.name}.png')

      if type == "jail":
        imageJail = Image.open("kiwibot/images/jail.png").convert("RGBA")
        imageJail = imageJail.resize((128, 128))
        user1_avatar = user1_avatar.resize((128, 128))
        user1_avatar.paste(imageJail, (0, 0), imageJail)
        user1_avatar.save(f'{type}{user.name}.png')    

      if type == "egg":
        imageEgg = Image.open("kiwibot/images/egg.jpg").convert("RGBA")
        user1_avatar = user1_avatar.resize((40, 40))
        user1_avatar = circle(user1_avatar, (40, 40))
        imageEgg.paste(user1_avatar, (43, 227), user1_avatar)
        imageEgg.save(f'{type}{user.name}.png')   

      if type == "gravestone":
        imageGravestone = Image.open("kiwibot/images/gravestone.png").convert("RGBA")
        user1_avatar = user1_avatar.resize((60, 60))
        imageGravestone.paste(user1_avatar, (60, 40), user1_avatar)
        imageGravestone.save(f'{type}{user.name}.png')          

      if type == "fedora":
        fedoraCanvas = Image.new("RGBA", (463, 441), (255, 255, 255, 0))
        imageFedora = Image.open("kiwibot/images/fedora.png").convert("RGBA")
        user1_avatar = user1_avatar.resize((253, 248))
        user1_avatar = circle(user1_avatar, (253, 248))
        fedoraCanvas.paste(user1_avatar, (125, 80), user1_avatar)
        fedoraCanvas.paste(imageFedora, (0, 0), imageFedora)
        fedoraCanvas.save(f'{type}{user.name}.png')     

      if type == "invert":
        user1_avatar = user1_avatar.resize((256, 256))
        user1_avatar = user1_avatar.convert('RGB')
        user1_avatar = ImageOps.invert(user1_avatar)
        user1_avatar.save(f'{type}{user.name}.png')             

      try:
        file=discord.File(f'{type}{user.name}.png')
        await ctx.respond(file=file)
        await asyncio.sleep(1)
        os.remove(f"{type}{user.name}.png")

      except:
        await ctx.respond(embed=embed)

    
    #TEXT
    @commands.slash_command(name="text", description=f"{cmdsdescription['text']}")
    @commands.cooldown(1, 10, commands.BucketType.user)
    @option(
      "type",
      autocomplete=discord.utils.basic_autocomplete(["emojify", "spoiler", "trumpet", "skull", "clap", "lowercase", "uppercase"]),
    )
    async def text(self, ctx, type : str, text : str):
      result = ""

      if type == "emojify":
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

          result = "".join(emojis)

      if type == "spoiler":
        for character in text:
          if character != " ":
            result += "||  " + character + "  ||" 

      if type == "trumpet":
        separator = "🎺"
        for character in text:
          if character != " ":
            result = result + separator + character
            
        result += separator       

      if type == "skull":
        separator = "💀"
        for character in text:
          if character != " ":
            result = result + separator + character
            
        result += separator       

      if type == "clap":
        separator = "👏"
        for character in text:
          if character != " ":
            result = result + separator + character
            
        result += separator  

      if type == "lowercase":
        result = text.lower()   

      if type == "uppercase":
        result = text.upper()             

      await ctx.respond(result)

    #RATE
    @commands.slash_command(name="rate", description=f"{cmdsdescription['rate']}")
    @commands.cooldown(1, 10, commands.BucketType.user)
    @option(
      "type",
      autocomplete=discord.utils.basic_autocomplete(["epicgamer", "thot", "gay", "simp", "stank", "retarded", "cool"]),
    )
    async def rate(self, ctx, type : str, user : discord.Member):  
        user = user or ctx.author
        rand = random.randint(0, 100)

        embed = discord.Embed(
          title="rate machine never lies",
          color=discord.Colour.blue()
        )   
        
        if type == "epicgamer":
          embed.title = "epic gamer rate machine never lies"
          embed.description = f"{user.display_name}, you are {rand}% epic gamer"

        if type == "thot":
          embed.title = "thot rate machine never lies"
          embed.description = f"{user.display_name}, you are {rand}% thotty"

        if type == "gay":
          embed.title = "gay rate machine never lies"
          if rand > 30:
            embed.description = f"{user.display_name}, you are {rand}% gay🏳️‍🌈"

          else:
            embed.description = f"{user.display_name}, you are {rand}% gay📏"

        if type == "simp":
          embed.title = "simp rate machine never lies"
          if rand > 30:
            embed.description = f"{user.display_name}, you are {rand}% simp.. You should be ashamed!"

          else:
            embed.description = f"{user.display_name}, you are {rand}% simp.. Very nice solider!"    

        if type == "stank":
          embed.title = "stank rate machine never lies"
          if rand > 15:
            embed.description = f"{user.display_name}, you are {rand}% stanky.. Wash your reproductive organ well you bastard!"

          else:
            embed.description = f"{user.display_name}, you are {rand}% stanky.. I'm amazed! You are washing your ass?"          

        if type == "retarded":
          embed.title = "retarded machine never lies"
          embed.description = f"{user.display_name}, you are {rand}% retarded"

        if type == "cool":
          embed.title = "cool machine never lies"
          embed.description = f"{user.display_name}, you are {rand}% cool"
          
        await ctx.respond(embed=embed)

      
    #STAPINESCU
    @commands.slash_command(name="dadjoke", description=f"{cmdsdescription['dadjoke']}")
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def dadjoke(self, ctx):
        embed = discord.Embed(
          title="just a dad joke",
          color = discord.Colour.blue()
        )
      
        page = requests.get("https://icanhazdadjoke.com/")
        soup = BeautifulSoup(page.text, 'html5lib')
        dadjoke = soup.find('div', {"class": "card-content"})

        embed.description = f"{dadjoke.text}"
      
        await ctx.respond(embed=embed)  
      
    #STAPINESCU
    @commands.slash_command(name="stapinescu", description=f"{cmdsdescription['stapinescu']}")
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def stapinescu(self, ctx):
        embed = discord.Embed(
          title="cuvinte celebre spuse de stapinu",
          color = discord.Colour.blue()
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
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def roast(self, ctx, member : discord.Member = None):
        member = member or ctx.author
        embed = discord.Embed(
          title="roast",
          color = discord.Colour.blue()
        )
      
        page = requests.get(f"https://insult.mattbas.org/api/insult.html?who={member.display_name}")
        soup = BeautifulSoup(page.text, 'html5lib')
        insult = soup.find('h1', {"class": "insult"})

        embed.description = f"{insult.text}"
      
        await ctx.respond(embed=embed)   

    #MEME
    @commands.slash_command(name="meme", description=f"{cmdsdescription['meme']}")
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def meme(self, ctx):
        embed = discord.Embed(
          title="meme",
           color = discord.Colour.blue()
          )
      
        req = requests.get("https://some-random-api.ml/meme")
        data = req.json()

        embed.set_image(url=data["image"])
      
        await ctx.respond(embed=embed)   
      
    #8BALL 
    @commands.slash_command(name="8ball", description=f"{cmdsdescription['8ball']}")
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def _8ball(self, ctx, question):
        embed = discord.Embed(
          title="8ball",
           color=discord.Colour.blue()
          )
      
        list = [
          'Yes! Are you retarded?',
          'Are you retarded? I am not Akinator..',
          'Probably', 
          "I am retarded and I don't know..",
          'NO, RETARD', 
          'Are you retarded?', 
          'Reload?',
          "This question doesn't have any sense..",
        ]
      
        answer = random.choice(list)
        embed.add_field(name="Question",value=f'{question}',inline=False)
        embed.add_field(name="Answer",value=f'{answer}',inline=False)
      
        await ctx.respond(embed=embed) 

    #HACK
    @commands.slash_command(name="hack", description=f"{cmdsdescription['hack']}")
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def hack(self, ctx, member : discord.Member):
        member = member or ctx.author

        await ctx.respond("STARTING..", delete_after=2)
        await asyncio.sleep(2)

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
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def pussy(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        
        choice = random.choice(['{}', '[{}]', '()', '[]', '({})', '{]', '[}'])
      
        embed = discord.Embed(
          title="pussy machine never lies",
          description=f"{member.name}'s pussy looks like this: \n{choice}",
          color=discord.Colour.blue()
        )

        await ctx.respond(embed=embed) 
      
    #PENIS
    @commands.slash_command(name="penis", description=f"{cmdsdescription['penis']}")
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def penis(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        rand = random.randint(1, 30)
        lenght = "=" * rand
      
        embed = discord.Embed(
          title="penis machine never lies",
          description = f"{member.display_name}'s penis \n8{lenght}>",
          color=discord.Colour.blue()
        )
      
        await ctx.respond(embed=embed) 


      
def setup(bot):
    bot.add_cog(Fun(bot))
