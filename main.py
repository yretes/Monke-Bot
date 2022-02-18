import discord
from keep_alive import keep_alive
import os
import datetime
import random
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType

client = commands.Bot(command_prefix='.')


DanceVids =[
  "Here I go!\nhttps://www.youtube.com/watch?v=S3iVkw44VXs",
  "Check me out!\nhttps://www.youtube.com/watch?v=OSrTw1mMyzU",
  "Can't stop, won't stop!\nhttps://www.youtube.com/watch?v=hEGYHSiX3H4",
  "Monkey Moves!\nhttps://www.youtube.com/watch?v=--rJ6Yf56LU",
  "Sure thing!\nhttps://www.youtube.com/watch?v=JFT18tcQV6A",
  "Don't have to ask twice!\nhttps://www.youtube.com/watch?v=0KQNZ_zQTak"
]

with open('quotes') as q:
  quotes=q.readlines()

Greetings=[
  ":monkey_face: Yooo! :monkey_face:\nhttps://media.giphy.com/media/RBDLuqxYZCCkM/giphy.gif",
  ":monkey_face: Yooo! :monkey_face:\nhttps://media.giphy.com/media/ylyUQlf4VUVF9odXKU/giphy.gif",
  ":monkey_face: Yooo! :monkey_face:\nhttps://media.giphy.com/media/5oYgxQKHhEjEk/giphy-downsized-large.gif",
  ":monkey_face: Yooo! :monkey_face:\nhttps://media.giphy.com/media/l0IyhaadlCzZzbovC/giphy.gif",
  ":monkey_face: Yooo! :monkey_face:https://media.giphy.com/media/R8s2pWPslY0dG/giphy.gif",
  ":monkey_face: Yooo! :monkey_face:https://media.giphy.com/media/ok41vsqh4pA6A/giphy.gif"
]

Wednesday=[
  ":frog: It is wednesday, my dudes :frog:\n\nhttps://www.youtube.com/watch?v=PE8GlPpuLuY",
  ":frog: It is wednesday, my dudes :frog:\n\nhttps://www.youtube.com/watch?v=Kz26jod9-cQ",
  ":frog: It is wednesday, my dudes :frog:\n\nhttps://www.youtube.com/watch?v=meuYC7FP7HU",
  ":frog: It is wednesday, my dudes :frog:\n\nhttps://www.youtube.com/watch?v=Xf_wuAQ-t44",
]

AvraeMessages=[
  "C'mon Avrae, gimme something good!",
  "Monke time!",
  "Funky Stats comin up!",
  "This is totally legit, I swear ;)"
]
actualDay = datetime.datetime.today()
dayFix=datetime.timedelta(hours=8)
day=actualDay+dayFix


@client.event
async def on_ready():
  print('{0.user} Online'.format(client))    

@client.event
async def on_message(message):

  if message.author==client.user:
    return

  if message.content.startswith('!monkechar'):
    await message.reply(random.choice(AvraeMessages),mention_author=False)
    await message.channel.send('@Monke Bot\nGenerated funky stats:\n4d6kh3 (6,6,6,~~6~~) = 18\n4d6kh3 (6,6,6,~~6~~) = 18\n4d6kh3 (6,6,6,~~6~~) = 18\n4d6kh3 (6,6,6,~~6~~) = 18\n4d6kh3 (6,6,6,~~6~~) = 18\n4d6kh3 (6,6,6,~~6~~) = 18\nTotal = 108 \n **You have returned to monke**')
    return

  if message.content.startswith('!yo'):
    await message.reply(random.choice(Greetings),mention_author=True)
    return
  
  if message.content.startswith('!CheckDay'):
    if day.weekday()==0:
       await message.channel.send(' :speak_no_evil: Darn... today is Monday... :speak_no_evil:  \n \n https://tenor.com/btIa7.gif')
       return
    if day.weekday()==1:
       await message.channel.send(':trolleybus: Woah its Trolley Tuesday! :trolleybus: \n\n https://www.youtube.com/watch?v=lUtuDMHVfgs')
       return
    if day.weekday()==2:
       await message.channel.send(random.choice(Wednesday))
       return
    if day.weekday()==3:
       await message.channel.send(' :see_no_evil: It is little Friday, also known as Thursday! SO CLOSE!! :see_no_evil:    \n \n https://tenor.com/9ep1.gif')
       return
    if day.weekday()==4:
      await message.channel.send(' :monkey_face: Today is Fonky Monkey Friday! :monkey_face: \n \n  https://www.youtube.com/watch?v=2FRBHyGqszA \n @here')
      return
    if day.weekday()==5:
      await message.channel.send(' :gorilla: Weekend! Sleep in, treat yourself to some good food. You earned it! :gorilla: \n \n https://www.youtube.com/watch?v=F2cFdniSNkM \n')
      return
    if day.weekday()==6:
      await message.channel.send(' :monkey_face: :selfie: Selfie Sunday, yall! Show those beautiful faces! :monkey_face: :selfie:  \n \n https://upload.wikimedia.org/wikipedia/commons/4/4e/Macaca_nigra_self-portrait_large.jpg')
      return
  
  if message.content.startswith('!dance'):
    await message.reply(random.choice(DanceVids),mention_author=True)
  if "Donkey Kong" in message.content:
    await message.reply(':gorilla:\n:necktie:', mention_author=True)
  if "donkey kong" in message.content:
    await message.reply(':gorilla:\n:necktie:', mention_author=True)
  if "Diddy Kong" in message.content:
    await message.reply(':billed_cap:\n:monkey_face:', mention_author=True)
  if "diddy kong" in message.content:
    await message.reply(':billed_cap:\n:monkey_face:', mention_author=True)
  if "Funky Kong" in message.content:
    await message.reply(':gorilla:\n:shirt:', mention_author=True)
  if "funky kong" in message.content:
    await message.reply(':gorilla:\n:shirt: ', mention_author=True)
  if "cranky kong" in message.content:
    await message.reply(':soon::skull:', mention_author=True)
  if "Cranky Kong" in message.content:
    await message.reply(':soon::skull:', mention_author=True)

  if "monke bot" in message.content:
    await message.reply(':monkey_face: Yooo! :monkey_face: You DID mention my name!', mention_author=True)
    return
  if "Monke bot" in message.content:
    await message.reply(':monkey_face: Yooo! :monkey_face: You DID mention my name!', mention_author=True)
    return
  if "monke Bot" in message.content:
    await message.reply(':monkey_face: Yooo! :monkey_face: You DID mention my name!', mention_author=True)
    return
  if "Monke Bot" in message.content:
    await message.reply(':monkey_face: Yooo! :monkey_face: You DID mention my name!', mention_author=True)
    return

  if "monke" in message.content:
    if "bot" in message.content:
      return
    if "Bot" in message.content:
      return
    await message.channel.send(':monkey: Someone mention my name?')
    return
  if "Monke" in message.content:
    if "bot" in message.content:
      return
    if "Bot" in message.content:
      return
    if "Commands" in message.content:
      return
    await message.channel.send(':monkey: Someone mention my name?')
    return

  if message.content.startswith('!quote'):
    await message.reply(random.choice(quotes))

  if message.content.startswith('!MonkeCommands'):
    await message.channel.send(':monkey_face: Yooo :monkey_face: \n Here are some monke commands: \n \n:monkey: !CheckDay - Checks if it is Fonky Monkey Friday yet? \n \n:monkey: !yo - If you want to greet the monke! \n \n:monkey: !quote - I will tell you a famous monkey quote! \n \n :monkey: !dance - If you want me to do a little dance \n \n:monkey: !MonkeCommands - Displays commands, but you already knew that, you smarty smart smart...' )

    await client.process_commands(message)
keep_alive()
token=os.environ.get('TOKEN')
client.run(token)
