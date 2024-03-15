import discord
from discord.ext import tasks, commands


class Fun(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.hybrid_command()
    async def colour(self, ctx: commands.Context, colour: discord.Colour):
        try:
            server = await self.bot.fetch_guild(ctx.guild.id)
            for role in ctx.author.roles:
                if role.name.startswith("c_"):
                    await ctx.author.remove_roles(role)
            role = await server.create_role(name=f"c_{colour}", colour=colour)
            await role.edit(position=10)
            await ctx.author.add_roles(role)
            await ctx.reply(f"Your colour has been set to {colour}.")
        except Exception as e:
            await ctx.reply(f"An error occurred: {e}")



async def setup(bot):
    await bot.add_cog(Fun(bot))
    print("Fun Cog loaded")


async def teardown(bot):
    print("Fun Cog unloaded")
    await bot.remove_cog(Fun(bot))
