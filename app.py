#!/usr/bin/python3 -u
import os
import yaml
import discord
from dotenv import load_dotenv
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
with open("data/spencer.yml", 'r') as stream:
    try:
        spencer_quotes = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

client = discord.Client()


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

    if message.content == 'mud spencer':
        response = random.choice(spencer_quotes)
        await message.channel.send(response)

client.run(TOKEN)
