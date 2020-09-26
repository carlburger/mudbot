#!/usr/bin/python3 -u
import os
import discord
from dotenv import load_dotenv
import random

from mud.spencer import Spencer

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

spencer = Spencer()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Hi {member.name}, welcome to my Discord server!'
#     )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await spencer.on_message(message)


client.run(TOKEN)
