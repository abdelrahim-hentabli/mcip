import asyncio
import discord
from discord.ext import tasks, commands
import subprocess

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None, status=discord.Status.idle)

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ip = subprocess.run(["curl", "-s", "ifcfg.me"], capture_output=True).stdout.decode('UTF-8')

    @tasks.loop(minutes=5.0)
    async def change_status(self):
        self.ip = subprocess.run(["curl", "-s", "ifcfg.me"], capture_output=True).stdout.decode('UTF-8')
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Game(name=f"Minecraft @ IP: \"{self.ip}\" and Port: \"19132\""))

    @commands.Cog.listener()
    async def on_ready(self):
        self.change_status.start()


async def main():
    await bot.add_cog(MyCog(bot))
    await bot.start('MTI4MzIwNDA2MTgzNTAzODc3MQ.Gayyyo.BIL5IR-Ig67MkoIcZvCoM7GTLiRyLxwhhHl_xU')

asyncio.run(main())
