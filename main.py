import discord
import os
import datetime

client = discord.Client()
day = datetime.datetime.today().weekday()

print(datetime.datetime.today().weekday())

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author==client.user:
    return

  if message.content.startswith('!MonkeGreet'):
    await message.channel.send(' :monkey_face: Yooo! :monkey_face: ')
  
  if message.content.startswith('!day'):
    if day!=4:
       await message.channel.send(' :monkey: It is not Fonky Monkey Friday yet :monkey: ')
       return
    if day==4:
       await message.channel.send(' :monkey_face: Today is Fonky Monkey Friday! :monkey_face: \n \n  https://www.youtube.com/watch?v=2FRBHyGqszA')
       return
  
  if message.content.startswith('!MonkeCommands'):
    await message.channel.send(':monkey_face: Yooo :monkey_face: \n Here are some monke commands: \n \n:monkey: !day - Checks if it is Fonky Monkey Friday yet? \n \n:monkey: !MonkeGreet - If you want to greet the monke! \n \n:monkey: !MonkeCommands - Displays commands, but you already knew that, you smarty smart smart...')
    
client.run(os.getenv('TOKEN'))