import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

client = commands.AutoShardedBot(shard_count=1, command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
  print('Ready!')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(os.getenv("DISCORD_TOKEN"))