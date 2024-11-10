import discord
from discord.ext import commands
from constants import TOKEN

extensions = (
    'mybot',
)


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            intents=discord.Intents.all(),
            command_prefix=commands.when_mentioned_or('$ '),
            help_command=None,
        )

    async def setup_hook(self):
        for extension in extensions:
            await self.load_extension(f'extensions.{extension}')


def main():
    MyBot().run(TOKEN)


if __name__ == '__main__':
    main()
