import discord
from discord import app_commands
from discord.ext import commands

import constants


class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener(name='on_ready')
    async def on_ready(self):
        print('\033[34m== BOT is Ready ==\033[0m')
        print(f'Logged in as {self.bot.user.name} ({self.bot.user.id})')



async def setup(bot) -> None:
    await bot.add_cog(MyCog(bot))