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
        embed = Embed(title=get_rule_index(1), description=get_rule_value(1), colour=0x00FFFF, timestamp=datetime.utcnow())
        embed.set_author(name="Otakustan")
        await ctx.send(embed=embed)
        
    @command(name="rule3",aliases=["r3", "rle3"], hidden=True)
    async def rule3(self,ctx):
        embed = Embed(title=get_rule_index(2), description=get_rule_value(2), colour=0x00FFFF, timestamp=datetime.utcnow())
        embed.set_author(name="Otakustan")
        await ctx.send(embed=embed)

    @command(name="rule4",aliases=["r4", "rle4"], hidden=True)
    async def rule3(self,ctx):
        embed = Embed(title=get_rule_index(3), description=get_rule_value(3), colour=0x00FFFF, timestamp=datetime.utcnow())
        embed.set_author(name="Otakustan")
        await ctx.send(embed=embed)

    @command(name="rule5",aliases=["r5", "rle5"], hidden=True)
    async def rule3(self,ctx):
        embed = Embed(title=get_rule_index(4), description=get_rule_value(4), colour=0x00FFFF, timestamp=datetime.utcnow())
        embed.set_author(name="Otakustan")
        await ctx.send(embed=embed)

    @command(name="rule6",aliases=["r6", "rle6"], hidden=True)
    async def rule3(self,ctx):
        embed = Embed(title=get_rule_index(5), description=get_rule_value(5), colour=0x00FFFF, timestamp=datetime.utcnow())
        embed.set_author(name="Otakustan")
        await ctx.send(embed=embed)

    @command(name="rule7",aliases=["r7", "rle7"], hidden=True)
    async def rule3(self,ctx):
        embed = Embed(title=get_rule_index(6), description=get_rule_value(6), colour=0x00FFFF, timestamp=datetime.utcnow())
        embed.set_author(name="Otakustan")
        await ctx.send(embed=embed)

    @command(name="rule8",aliases=["r8", "rle8"], hidden=True)
    async def rule3(self,ctx):
        embed = Embed(title=get_rule_index(7), description=get_rule_value(7), colour=0x00FFFF, timestamp=datetime.utcnow())
        embed.set_author(name="Otakustan")
        await ctx.send(embed=embed)

    @command(name="rule9",aliases=["r9", "rle9"], hidden=True)
    async def rule3(self,ctx):
        embed = Embed(title=get_rule_index(8), description=get_rule_value(8), colour=0x00FFFF, timestamp=datetime.utcnow())
        embed.set_author(name="Otakustan")
        await ctx.send(embed=embed)

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.command_ready.ready_up("rules")

def setup(bot):
    bot.add_cog(Rules(bot))