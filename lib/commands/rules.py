from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed
from datetime import datetime
from lib.utils.rule import get_rule_index, get_rule_value

class Rules(Cog):
    def __init__(self,bot):
        self.bot = bot

    @command(name="rule1",aliases=["r1", "rle1"], hidden=True)
    async def rule1(self,ctx):
        embed = Embed(title=get_rule_index(0), description=get_rule_value(0), colour=0x00FFFF, timestamp=datetime.utcnow())
        embed.set_author(name="Otakustan")
        await ctx.send(embed=embed)

    @command(name="rule2",aliases=["r2", "rle2"], hidden=True)
    async def rule2(self,ctx):
        embed = Embed(title="Rule 02", description="No Spam, neither in text channels nor in voice channels.", colour=0x00FFFF, timestamp=datetime.utcnow())
        embed.set_author(name="Otakustan")
        await ctx.send(embed=embed)
        
    @command(name="rule3",aliases=["r3", "rle3"], hidden=True)
    async def rule3(self,ctx):
        embed = Embed(title="Rule 03", description="No Spam, neither in text channels nor in voice channels.", colour=0x00FFFF, timestamp=datetime.utcnow())
        embed.set_author(name="Otakustan")
        await ctx.send(embed=embed)

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.command_ready.ready_up("rules")

def setup(bot):
    bot.add_cog(Rules(bot))