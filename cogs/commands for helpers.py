import discord
from discord.ext import commands
import botdata
import time
import actions

data = botdata.d
emoji = botdata.e
client = data.client

class CommandsForHelpers(commands.Cog):
    def __init__(self, client):
        self.client = client

    # update
    @commands.command()
    async def update(self, ctx):
        pc = await actions.permission_check(ctx, 'HELPER')
        if pc == True:
            if ctx.message.guild.id == int(data.community[0]):
                role = ctx.message.guild.get_role(botdata.r.rx_updates)
            elif ctx.message.guild.id == int(data.support[0]):
                role = ctx.message.guild.get_role(botdata.r.rxs_updates)
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

    # daily <question>
    @commands.command()
    async def daily(self, ctx, *, text = None):
        pc = await actions.permission_check(ctx, 'HELPER')
        if pc == True:
            if text == None:
                await actions.say(ctx.message.channel, '{} No question given.'.format(emoji.error))
            elif len(text) > 150:
                await actions.say(ctx.message.channel, '{} The question cannot be longer than 150 characters.'.format(emoji.error))
            elif '?' not in text:
                await actions.say(ctx.message.channel, '{} Make sure to spell the question correctly.\n{} Try again with proper grammar and a question mark at the end.'.format(emoji.srt_right, emoji.error))
            else:
                h = await actions.say(ctx.message.channel, '{} Creating new question...'.format(emoji.loading_circle))
                question = ''
                answers = {}
                votes = []
                delete = []
                async for i in client.get_channel(botdata.c.rx_daily).history(limit=data.limit):
                    if not i.author.bot and len(i.attachments) == 0 and not i.pinned:
                        for u in i.reactions:
                            if str(u.emoji) == emoji.upvote:
                                votes.append(u.count)
                                answers[str(i.author.id)] = [i.content, u.count]
                                break
                        delete.append(i)
                    elif i.author.id == client.user.id:
                        question += i.content.replace('<@&{}>'.format(botdata.r.rx_daily), '')
                        delete.append(i)
                votes.sort()
                votes.reverse()
                m = ':grey_question: **Last question:**{}'.format(question)
                m += '\n'
                m += '\n{} **Top answers:**'.format(emoji.srt_right)
                msgs = []
                for i in votes:
                    for u in answers:
                        if answers[u][1] == i:
                            msgs.append('<@{}>\n{}{} {}\n{}{} __{} vote(s)!__'.format(u, emoji.blank, emoji.srt_right, answers[u][0], emoji.blank, emoji.srt_right, i))
                            file = data.mclient['MAIN']['upvotes'].find_one({'user' : u})
                            if file == None:
                                data.mclient['MAIN']['upvotes'].insert_one({'user' : u, 'upvotes' : i})
                            else:
                                data.mclient['MAIN']['upvotes'].update_one({'user' : u}, {'$set' : {'upvotes' : int(file['upvotes']) + 1}})
                            del answers[u]
                            break
                m += '\n:crown: {}'.format(msgs[0])
                m += '\n:trophy: {}'.format(msgs[1])
                m += '\n:trident: {}'.format(msgs[2])
                role = ctx.message.guild.get_role(botdata.r.rx_daily)
                await role.edit(mentionable=True)
                await actions.say(client.get_channel(botdata.c.rx_daily), m, content='<@&{}>\n{}'.format(role.id, text))
                await role.edit(mentionable=False)
                await client.get_channel(botdata.c.rx_daily).delete_messages(delete)
                await actions.edit(h, '{} New daily question created!'.format(emoji.worked))
                l = '{} **Daily question:**'.format(emoji.log)
                l += '\n'
                l += '\n{} `Created by:` <@{}> ( {} ### {} )'.format(emoji.srt_right, ctx.message.author.id, ctx.message.author, ctx.message.author.id)
                l += '\n{} `Question:` {}'.format(emoji.srt_right, text)
                await actions.send_log(ctx.message, l)
                    
def setup(client):
    client.add_cog(CommandsForHelpers(client))
