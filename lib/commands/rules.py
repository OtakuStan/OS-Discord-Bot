from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed
from datetime import datetime
from lib.utils.rule import get_rule_index, get_rule_value, get_all_rules

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
    async def rule4(self,ctx):
        embed = Embed(title=get_rule_index(3), description=get_rule_value(3), colour=0x00FFFF, timestamp=datetime.utcnow())
        embed.set_author(name="Otakustan")
        await ctx.send(embed=embed)

    @command(name="rule5",aliases=["r5", "rle5"], hidden=True)
    async def rule5(self,ctx):
        embed = Embed(title=get_rule_index(4), description=get_rule_value(4), colour=0x00FFFF, timestamp=datetime.utcnow())
        embed.set_author(name="Otakustan")
        await ctx.send(embed=embed)

    @command(name="rule6",aliases=["r6", "rle6"], hidden=True)
    async def rule6(self,ctx):
        embed = Embed(title=get_rule_index(5), description=get_rule_value(5), colour=0x00FFFF, timestamp=datetime.utcnow())
        embed.set_author(name="Otakustan")
        await ctx.send(embed=embed)

    @command(name="rule7",aliases=["r7", "rle7"], hidden=True)
    async def rule7(self,ctx):
        embed = Embed(title=get_rule_index(6), description=get_rule_value(6), colour=0x00FFFF, timestamp=datetime.utcnow())
        embed.set_author(name="Otakustan")
        await ctx.send(embed=embed)

    @command(name="rule8",aliases=["r8", "rle8"], hidden=True)
    async def rule8(self,ctx):
        embed = Embed(title=get_rule_index(7), description=get_rule_value(7), colour=0x00FFFF, timestamp=datetime.utcnow())
        embed.set_author(name="Otakustan")
        await ctx.send(embed=embed)

    @command(name="rule9",aliases=["r9", "rle9"], hidden=True)
    async def rule9(self,ctx):
        embed = Embed(title=get_rule_index(8), description=get_rule_value(8), colour=0x00FFFF, timestamp=datetime.utcnow())
        embed.set_author(name="Otakustan")
        await ctx.send(embed=embed)

    @command(name="rule10",aliases=["r10", "rle10"], hidden=True)
    async def rule10(self,ctx):
        embed = Embed(title=get_rule_index(9), description=get_rule_value(9), colour=0x00FFFF, timestamp=datetime.utcnow())
        embed.set_author(name="Otakustan")
        await ctx.send(embed=embed)

    @command(name="rule11",aliases=["r11", "rle11"], hidden=True)
    async def rule11(self,ctx):
        embed = Embed(title=get_rule_index(10), description=get_rule_value(10), colour=0x00FFFF, timestamp=datetime.utcnow())
        embed.set_author(name="Otakustan")
        await ctx.send(embed=embed)

    @command(name="rule12",aliases=["r12", "rle12"], hidden=True)
    async def rule12(self,ctx):
        embed = Embed(title=get_rule_index(11), description=get_rule_value(11), colour=0x00FFFF, timestamp=datetime.utcnow())
        embed.set_author(name="Otakustan")
        await ctx.send(embed=embed)

    @command(name="rule13",aliases=["r13", "rle13"], hidden=True)
    async def rule13(self,ctx):
        embed = Embed(title=get_rule_index(12), description=get_rule_value(12), colour=0x00FFFF, timestamp=datetime.utcnow())
        embed.set_author(name="Otakustan")
        await ctx.send(embed=embed)

    @command(name="ruleall",aliases=["rall", "rleall"], hidden=True)
    async def rule13(self,ctx):
        allRules = get_all_rules()
        embed = Embed(title="All Rules", description="Don't forget to follow the rules!!", colour=0x00FFFF, timestamp=datetime.utcnow())
        for index, rule in allRules.items():
            embed.add_field(name=index, value=rule)
        embed.set_author(name="Otakustan")
        await ctx.send(embed=embed)

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.command_ready.ready_up("rules")

def setup(bot):
    bot.add_cog(Rules(bot))