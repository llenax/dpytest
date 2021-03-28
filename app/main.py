import os
import discord
from discord.ext import commands

from flask import Flask
app= Flask(__name__)
@app.route('/')
def index():
  return "<h1>Welcome to CodingX</h1>"

client = commands.AutoShardedBot(shard_count=1, command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
  print('Ready!')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
