import discord
from discord.ext import commands
import botdata
import time
import actions

data = botdata.d
emoji = botdata.e
client = data.client

class CommandsForAdmins(commands.Cog):
    def __init__(self, client):
        self.client = client

    # resetlb
    @commands.command(aliases=['rlb'])
    async def resetlb(self, ctx):
        pc = await actions.permission_check(ctx, 'ADMIN')
        if pc == True:
            data.mclient['MAIN']['messages'].delete_many({})
            data.mclient['MAIN']['partnerships'].delete_many({})
            data.mclient['MAIN']['upvotes'].delete_many({})
            await actions.say(ctx.message.channel, '{} All leaderboards have been reset.'.format(emoji.worked))
            await actions.send_log(ctx.message, '{} **Leaderboards reset:**\n\n{} `Reset by:` <@{}> ( {} ### {} )'.format(emoji.log, emoji.srt_right, ctx.message.author.id, ctx.message.author, ctx.message.author.id))

def setup(client):
    client.add_cog(CommandsForAdmins(client))
