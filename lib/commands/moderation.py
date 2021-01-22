from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed, File
from random import choice
from datetime import datetime


class Command(Cog):
    def __init__(self,bot):
        self.bot = bot

    @command(name="ban", aliases=["b"], hidden=True)
    @commands.has_permissions(ban_members = True)
    async def ban(ctx, member : discord.Member, *, reason = None):
       await member.ban(reason = reason)
    
    @command(name="ban", aliases=["b"], hidden=True)
    @commands.has_permissions(administrator = True)
    async def unban(ctx, *, member):
      banned_users = await ctx.guild.bans()
      member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return
    
    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.command_ready.ready_up("commands")

def setup(bot):
    bot.add_cog(Command(bot))
    
