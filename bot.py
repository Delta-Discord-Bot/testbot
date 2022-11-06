import os
from typing import Optional

import discord
from discord.ext import commands
from dotenv import load_dotenv

intens = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intens)
load_dotenv()

TOKEN: Optional[str] = os.getenv("TOKEN")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print('Bot is ready.')


@bot.command(name='ping')
async def ping(ctx: commands.Context):
    await ctx.send('Pong!')

assert TOKEN is not None

bot.run(TOKEN)