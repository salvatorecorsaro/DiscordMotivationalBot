import discord
import os
import requests
import json
import random

# In order for the bot to work you have to insert a valid bot token from discord developers in the .env file


client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

starter_encouragements = [
  "Cheer up!",
  "You are fantastic!",
  "Keep it up!",
  "Never surrender"
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")

  json_data = json.loads(response.text)
  quote = json_data[0]['q']  + ' - ' + json_data[0]['a']

  return(quote)

@client.event
async def on_ready():
  print('We have logged in as{0.user}'.format(client))

@client.event
async def on_message(message):

  msg = message.content

  if message.author == client.user:
    return
  if msg.startswith('$hello'):
    await message.channel.send('Hello!')

  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))

client.run(os.getenv('TOKEN'))