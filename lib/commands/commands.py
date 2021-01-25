from discord.ext.commands import Cog
from discord.ext.commands import command, has_permissions
from discord import Embed, File
from discord import Member
from random import choice
from datetime import datetime

class Command(Cog):
    def __init__(self,bot):
        self.bot = bot

    @command(name="hello", aliases=["hola", "h"], hidden=True)
    async def say_hello(self, ctx):
        await ctx.send(f"{choice(('Konnichiva', 'Ara Ara', 'Okaeri', 'Yahallo'))} {ctx.author.mention}!")

    @command(name="callme", aliases=["call", "c"], hidden=True)
    async def call_me(self, ctx, *, message):
        # await ctx.message.delete()
        await ctx.send(f"{ctx.author.mention} {message}")

    @command(name="helpme", aliases=["HELP", "helpu"])
    async def command_help(self,ctx):
        embed = Embed(title="Command Help", description="Prefix = & |Commands - inspire , Date , OtakuStanRecorder , sbcount , Reddit , sub , stats , instaDareChan , instaUtkarsh , instaOmi , instaSatoshi , instaSubham , instaVoid , instaShinko , instaArpit , instaOrange , InstaOS , OfficialTwitter , FBpage , FBgroup , OtakuStanMembers , DiscordAdmin , DiscordMods , DiscordTMod , WordsFromCreator , YTneta , rulezero , rule01 , rule2 , rule3 , rule4 , rule5 , rule6 , rule7 , rule8 , rule9 , rule10 , rule11 , rule12 , ruleall", colour=0x00FFFF, timestamp=datetime.utcnow())
        embed.set_author(name="Otakustan")
        await ctx.send(embed=embed)

    # @command(name="echo", aliases=["say", "shout"])
    # async def echo_message(self, ctx, *, message):
    #     await ctx.message.delete()
    #     await ctx.send(message)
    
    # working say implementation
    @command(name="echo", aliases=["shout", "say"])                   
    async def say( self, ctx, *args):
        mesg = ' '.join(args)
        await ctx.send(mesg)

    # Moderation
                       
    @command(name="ban", aliases=["b"], hidden=True)
    @has_permissions(ban_members = True)
    async def ban(self, ctx, member : Member, *, reason = None):
       await member.ban(reason = reason)
    
    @command(name="unban", aliases=["ub"], hidden=True)
    @has_permissions(administrator = True)
    async def unban(self, ctx, *, member):
      banned_users = await ctx.guild.bans()
      member_name, member_discriminator = member.split("#")
      for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return
## error handling
    @command.event
    async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all requirements :pleading:.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have all the requirements :angry:")
                       
                      
                       
                       
    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.command_ready.ready_up("commands")

def setup(bot):
    bot.add_cog(Command(bot))
