from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed
from datetime import datetime

class Rules(Cog):
    def __init__(self,bot):
        self.bot = bot

    @command(name="rule1",aliases=["r1", "rle1"], hidden=True)
    async def rule1(self,ctx):
        embed = Embed(title="Rule 01", description="Stay Respectful!!", colour=0x00FFFF, timestamp=datetime.utcnow())
        embed.set_author(name="Otakustan")
        await ctx.send(embed=embed)

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.command_ready.ready_up("rules")

def setup(bot):
    bot.add_cog(Rules(bot))