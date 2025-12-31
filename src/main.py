import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord import app_commands

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GENERAL_CHANNEL_ID = int(os.getenv("GENERAL_CHANNEL_ID"))

if TOKEN is None:
    raise RuntimeError("DISCORD_TOKEN is not set")


class Client(commands.Bot):  # Look into classes
    async def on_ready(self):  # on_ready is predefined function in discord.py
        print(f'Logged on as {self.user}!')  # Log on as the name as the bot

        try:
            guild = discord.Object(id=GENERAL_CHANNEL_ID)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guid {guild.id}')
        except Exception as e:
            print(f'Error syncing commands: {e}')

    async def on_message(self, message):  # Predefined, mesg sent in server
        if message.author == self.user:
            return  # Bot can't reply to itself
        if message.content.startswith('hello'):
            await message.channel.send(f'Hi there {message.author}')

    async def on_reaction_add(self, reaction, user):
        await reaction.message.channel.send('You reacted')


intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)

GUILD_ID = discord.Object(id=GENERAL_CHANNEL_ID)


@client.tree.command(name="test",
                     description="Testing slash commands...",
                     guild=GUILD_ID)
async def tryTest(interaction: discord.Interaction):
    await interaction.response.send_message("This is a test of slash command")


@client.tree.command(name="function",
                     description="Testing slash arguments...",
                     guild=GUILD_ID)
async def tryPrint(interaction: discord.Interaction, printer: str):
    await interaction.response.send_message(printer)

client.run(TOKEN)
