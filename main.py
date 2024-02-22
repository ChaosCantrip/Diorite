import asyncio
import os
from datetime import datetime

import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents, case_insensitive=True)


@bot.event
async def on_ready():
    """Runs when the bot is ready."""

    # Print a message to the console
    print(f"Logged in as {bot.user.name} ({bot.user.id})")

    # Create an embed to send to the bot owner
    embed = discord.Embed(
        title=f"{bot.user.display_name} is up and running!",
        description=f"<t:{int(datetime.now().timestamp())}:F>",
        colour=discord.Colour.green()
    )
    embed.set_thumbnail(url=bot.user.display_avatar.url)

    # Send the embed to the bot owner
    app_info = await bot.application_info()
    owner = app_info.owner
    await owner.send(embed=embed)


async def main():
    async with bot:
        await bot.start(os.environ.get("DISCORD_TOKEN"))


asyncio.run(main())
