import os
import discord
from discord import Intents
from discord.ext import commands
from openai_handler import openai_handler
from google.cloud import secretmanager




# Print the secret payload (be cautious with this in production environments).
#print(f"Plaintext: {payload}")


# Initialize Discord client
intents = Intents.default()
client = discord.Client(intents=intents)

def connectto_discord():
# GCP project in which to store secrets in Secret Manager.
    project_id = "formal-stratum-411512"

# ID of the secret to access.
    secret_id = "DISCORD_TOKEN"

# Version of the secret to access.
    secret_version = "1"  # Assuming you want to access the first version

# Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

# Form the resource name of the secret version.
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{secret_version}"

# Access the secret version.
    response = client.access_secret_version(request={"name": name})

# Extract the payload as a string.
    DISCORD_TOKEN = response.payload.data.decode("UTF-8")
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