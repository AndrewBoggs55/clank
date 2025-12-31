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

    async def on_message(self, message):  # Predefined, mesg sent in server
        if message.author == self.user:
            return  # Bot can't reply to itself
        if message.content.startswith('hello'):
            await message.channel.send(f'Hi there {message.author}')

    async def on_reaction_add(self, reaction, user):
        await reaction.message.channel.send('You reacted')


intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run(TOKEN)
