from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed
from datetime import datetime

class Insta(Cog):
    def __init__(self,bot):
        self.bot = bot

    @command(name="instadarechan", aliases=["idare", "instadare"])
    async def instaDare(self,ctx):
        embed = Embed(title="Follow Dare Chan on Instagram", description="https://www.instagram.com/darechandesu/?hl=en", colour=0x00FFFF, timestamp=datetime.utcnow())
        await ctx.send(embed=embed)

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.command_ready.ready_up("insta")

def setup(bot):
    bot.add_cog(Insta(bot))