import asyncio
import os
from datetime import datetime
import colorama

import discord
from discord.ext import commands

# ===== Setup =====

# Set up colorama
colorama.init(autoreset=True)

# Set up the bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents, case_insensitive=True)


# ===== Bot Events =====


@bot.event
async def on_ready():
    """Runs when the bot is ready."""

    # Print a message to the console
    print(colorama.Fore.GREEN + colorama.Style.BRIGHT + f"\n{bot.user.display_name} connected to Discord")
    print(colorama.Fore.MAGENTA + colorama.Style.BRIGHT + f"- Account: {bot.user}")
    print(colorama.Fore.MAGENTA + colorama.Style.BRIGHT + f"- User ID: {bot.user.id}")

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


# ===== Bot Commands =====

@bot.command()
async def ping(ctx: commands.Context):
    """Check the bot's latency."""
    await ctx.reply(f"Pong!\n`{round(bot.latency * 1000)}ms`")


@bot.command()
@commands.is_owner()
async def reboot(ctx: commands.Context):
    """Reboot the bot."""
    await ctx.reply("Alright! Rebooting now!")
    await bot.close()
    # Create flag file to signal the launcher script to reboot the bot
    with open("reboot", "w+") as f:
        f.write("")
    # Rebooting the bot is handled by the launcher script


@bot.command()
@commands.is_owner()
async def restart(ctx: commands.Context):
    """Restart the bot."""
    await ctx.reply("Alright! Restarting now!")
    await bot.close()
    # Create flag file to signal the launcher script to restart the bot
    with open("restart", "w+") as f:
        f.write("")
    # Restarting the bot is handled by the launcher script


@bot.command()
@commands.is_owner()
async def maintenance(ctx: commands.Context):
    """Put the bot into maintenance mode."""
    await ctx.reply("Alright! Putting the bot into maintenance mode now!")
    await bot.close()
    # The launcher script will automatically restart the bot in maintenance mode if no other flags are present


@bot.command()
@commands.is_owner()
async def pull(ctx: commands.Context):
    """Pull the latest commits from the repository."""
    # Reply to acknowledge the command
    message_text = "Pulling latest commits..."
    message = await ctx.reply(f"```{message_text}```")

    # Run the git pull command and send the output
    message_text += "\n\n" + os.popen("git pull").read()[0:3000]
    await message.edit(content=f"```{message_text}```")


# ===== Run Diorite =====

async def main():
    print(colorama.Fore.YELLOW + "Initialising Diorite...")
    async with bot:
        await bot.start(os.environ.get("DISCORD_TOKEN"))


asyncio.run(main())
