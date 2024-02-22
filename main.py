import asyncio
import os

import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents, case_insensitive=True)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} ({bot.user.id})")


async def main():
    async with bot:
        await bot.start(os.environ.get("DISCORD_TOKEN"))


asyncio.run(main())
