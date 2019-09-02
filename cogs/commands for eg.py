import discord
from discord.ext import commands
import botdata
import time
import actions

data = botdata.d
emoji = botdata.e
client = data.client

class CommandsForEG(commands.Cog):
    def __init__(self, client):
        self.client = client

    # event
    @commands.command()
    async def event(self, ctx):
        pc = await actions.permission_check(ctx, 'EG')
        if pc == True:
            role = ctx.message.guild.get_role(botdata.r.rx_events)
            if role.mentionable == True:
                await role.edit(mentionable=False)
                await actions.say(ctx.message.channel, '{} <@&{}> can no longer be mentioned.'.format(emoji.off, role.id))
            else:
                await role.edit(mentionable=True)
                await actions.say(ctx.message.channel, '{} <@&{}> can now be mentioned.'.format(emoji.on, role.id))
            l = '{} **Role mention toggled:**'.format(emoji.log)
            l += '\n'
            l += '\n{} `Toggled by:` <@{}> ( {} ### {} )'.format(emoji.srt_right, ctx.message.author.id, ctx.message.author, ctx.message.author.id)
            l += '\n{} `Role:` <@&{}> ( {} ### {} )'.format(emoji.srt_right, role.id, role.name, role.id)
            l += '\n{} `Mentionable:` {}'.format(emoji.srt_right, role.mentionable)
            await actions.send_log(ctx.message, l)

    # giveaway
    @commands.command()
    async def giveaway(self, ctx):
        pc = await actions.permission_check(ctx, 'EG')
        if pc == True:
            role = ctx.message.guild.get_role(botdata.r.rx_giveaways)
            if role.mentionable == True:
                await role.edit(mentionable=False)
                await actions.say(ctx.message.channel, '{} <@&{}> can no longer be mentioned.'.format(emoji.off, role.id))
            else:
                await role.edit(mentionable=True)
                await actions.say(ctx.message.channel, '{} <@&{}> can now be mentioned.'.format(emoji.on, role.id))
            l = '{} **Role mention toggled:**'.format(emoji.log)
            l += '\n'
            l += '\n{} `Toggled by:` <@{}> ( {} ### {} )'.format(emoji.srt_right, ctx.message.author.id, ctx.message.author, ctx.message.author.id)
            l += '\n{} `Role:` <@&{}> ( {} ### {} )'.format(emoji.srt_right, role.id, role.name, role.id)
            l += '\n{} `Mentionable:` {}'.format(emoji.srt_right, role.mentionable)
            await actions.send_log(ctx.message, l)
        
def setup(client):
    client.add_cog(CommandsForEG(client))
