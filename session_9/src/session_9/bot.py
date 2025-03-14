# This example requires the 'message_content' intent.
import os
import discord
from dotenv import load_dotenv

load_dotenv() 

serverID = 1349825314678771763
channelID = 1349825314678771766

intents = discord.Intents.default()
intents.message_content = True
intents.members=True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('hello, how are you doing?')

@client.event
async def on_member_join(member):
  guild = client.get_guild(serverID)
  channel = guild.get_channel(channelID)
  if channel:  
    emb = discord.Embed(title="NEW MEMBER",description=f"Thanks {member.name} for joining!")
    emb.set_thumbnail(url=member.avatar)
    await channel.send(member.mention, embed=emb)

  else:
    print("Channel not found")

def run():
    client.run(os.getenv('DISCORD_TOKEN',None))