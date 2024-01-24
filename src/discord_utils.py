import os
import discord
from discord import Intents
from discord.ext import commands
from openai_handler import openai_handler



# Initialize Discord client
intents = Intents.default()
client = discord.Client(intents=intents)

def connectto_discord():

    # Initialize Discord client
    intents = Intents.default()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('!ask'):
        # Get response from OpenAI
            response = openai_handler(message.content[5:])
        
        
            await message.channel.send(response.choices[0].text.strip())

    client.run(DISCORD_TOKEN)
