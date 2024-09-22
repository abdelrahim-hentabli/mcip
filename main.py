import asyncio
import discord
from discord.ext import tasks, commands
import subprocess
import re

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None, status=discord.Status.idle)

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ip = ""
        self.regex = re.compile("\d*\.\d*\.\d*\.\d*")

    @tasks.loop(minutes=5.0)
    async def change_status(self):
        potential_ip = subprocess.run(["curl", "-s", "ifcfg.me"], capture_output=True).stdout.decode('UTF-8')

        if self.regex.fullmatch(potential_ip) is not None:
            if (potential_ip != self.ip):
                self.ip = potential_ip
                print(f"IP changed to {self.ip}")
                channel = self.bot.get_channel(1287120247924723784)
                await channel.send(f"Minecraft Server IP Address Changed to: \"{self.ip}\" and Port: \"19132\"")
                await self.bot.change_presence(status=discord.Status.online, activity=discord.Game(name=f"Minecraft @ IP: \"{self.ip}\" and Port: \"19132\""))
        else:
            await self.bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=f"Minecraft @ IP: \"{self.ip}\" and Port: \"19132\""))

    @commands.Cog.listener()
    async def on_ready(self):
        self.change_status.start()


async def main():
    await bot.add_cog(MyCog(bot))
    await bot.start('MTI4MzIwNDA2MTgzNTAzODc3MQ.Gayyyo.BIL5IR-Ig67MkoIcZvCoM7GTLiRyLxwhhHl_xU')

asyncio.run(main())
