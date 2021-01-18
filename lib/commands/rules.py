from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed
from datetime import datetime

class Rules(Cog):
    def __init__(self,bot):
        self.bot = bot
        self.rules = {
            "Rule01": "Stay Respectful!!",
            "Rule02": "No Spam, neither in text channels nor in voice channels.",
            "Rule03": "No Abusing/Trash Talking (Aliases like frick, BC, MC are allowed).",
            "Rule04": "No impersonation.",
            "Rule05": "No politics or religious talks in chat.",
            "Rule06": "No Racism (this includes offensive memes that have an overall negative connotation, including the n word)",
            "Rule07": "Don't yell into your mic or be obnoxious while using the VC channels during events.",
            "Rule08": "Requesting members to avoid regional language in the group because most of the people wouldn't  know your language.",
            "Rule09": "Discussing newly released episode or any chapter from manga is allowed only in  #🤫︱spoiler-chat",
            "Rule10": "No NSFW",
            "Rule11": "No NSFW nicknames",
            "Rule12": "Please try not to be mean to other humans and bots.",
            "Rule13": "Must follow all the Discord's Terms of Service (Discord TOS - https://discord.com/terms)",
        }

    @command(name="rule1",aliases=["r1", "rle1"], hidden=True)
    async def rule1(self,ctx):
        embed = Embed(title="Rule01", description="Stay Respectful!!", colour=0x00FFFF, timestamp=datetime.utcnow())
        embed.set_author(name="Otakustan")
        await ctx.send(embed=embed)

    @command(name="rule2",aliases=["r2", "rle2"], hidden=True)
    async def rule1(self,ctx):
        embed = Embed(title="Rule 02", description="No Spam, neither in text channels nor in voice channels.", colour=0x00FFFF, timestamp=datetime.utcnow())
        embed.set_author(name="Otakustan")
        await ctx.send(embed=embed)

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.command_ready.ready_up("rules")

def setup(bot):
    bot.add_cog(Rules(bot))