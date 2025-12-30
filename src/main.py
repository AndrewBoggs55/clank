import os
from dotenv import load_dotenv
import discord

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

if TOKEN is None:
    raise RuntimeError("DISCORD_TOKEN is not set")


class Client(discord.Client):  # Look into classes
    async def on_ready(self):  # on_ready is predefined function in discord.py
        print(f'Logged on as {self.user}!')  # Log on as the name as the bot

    async def on_message(self, message):  # Predefined, called when mesg sent in server
        print(f'Mesage from {message.author}: {message.content}')  # prints msg from server into term

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run(TOKEN)
