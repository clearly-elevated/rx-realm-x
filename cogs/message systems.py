import discord
from discord.ext import commands
import botdata
import time
import actions
import asyncio
import random

data = botdata.d
emoji = botdata.e
client = data.client
counter = []

class MessageSystems(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, msg):
        if not msg.author.bot:
            # ANTI PING
            if '<@{}>'.format(client.user.id) in msg.content:
                await msg.channel.send('<:Ping:580090129063084043>')
            
            # DAILY QUESTIONS
            if msg.channel.id == botdata.c.rx_daily:
                async for i in msg.channel.history(limit=data.limit, before=msg):
                    if len(i.attachments) == 0 and not i.pinned and i.author.id == msg.author.id:
                        await msg.delete()
                        h = await actions.say(msg.channel, '{} You\'ve already sent an answer.\n{} You can always edit it.'.format(emoji.error, emoji.srt_right), content='<@{}>'.format(msg.author.id))
                        await asyncio.sleep(10)
                        return await h.delete()
                await msg.add_reaction(emoji.upvote.replace('<', '').replace('>', ''))

            # CONFESSIONS
            elif msg.channel.id == botdata.c.rx_confessions:
                if '#Me' in msg.content:
                    await actions.say(msg.channel, '{}\n\n{} `Posted by:` <@{}>'.format(msg.content.replace('#Me', ''), emoji.srt_right, msg.author.id))
                else:
                    await actions.say(msg.channel, '{}\n\n{} `This confession is anonymous`.'.format(msg.content, emoji.srt_right))
                await msg.delete()

            # PRIVATE VENT/RANT
            elif msg.guild == None:
                file = data.mclient['MAIN']['venting'].find_one({'user' : str(msg.author.id)})
                if msg.content.lower() == 'vent' or msg.content.lower() == 'ramt':
                    if file == None:
                        code = 'abcdefghijklmnopqrstuvwxyz0123456789'
                        tag = ''
                        for i in range(400):
                            tag += random.choice(code)
                            if len(tag) == 4:
                                f = data.mclient['MAIN']['venting'].find_one({'tag' : tag})
                                if f == None:
                                    break
                                else:
                                    tag = ''
                        data.mclient['MAIN']['venting'].insert_one({'user' : str(msg.author.id), 'tag' : tag})
                        m = '{} Private venting turned on.\n{} Your venting tag is `{}`.'.format(emoji.on, emoji.srt_right, tag)
                        m += '\n\n{} Any message you send in these DMs will be sent to the venting channel anonymously.\n{} To turn off private venting say `vent` again.'.format(emoji.srt_right, emoji.srt_right)
                        await actions.say(msg.author, m)
                        await actions.say(client.get_channel(botdata.c.rx_vent), '{} User `{}` turned on private venting.\n{} To talk to them your messages must start with `{}`.'.format(emoji.on, tag, emoji.srt_right, tag), content='<@&{}>'.format(botdata.r.rx_care))
                    else:
                        await actions.say(msg.author, '{} Private venting turned off.'.format(emoji.off))
                        m = '{} User `{}` turned off private venting.'.format(emoji.off, file['tag'])
                        data.mclient['MAIN']['venting'].delete_one({'user' : str(msg.author.id)})
                        await actions.say(client.get_channel(botdata.c.rx_vent), m)
                elif file != None:
                    await client.get_channel(botdata.c.rx_vent).send('{} **User `{}`:**\n{}'.format(emoji.srt_right, file['tag'], msg.content))
                    await actions.say(msg.author, '{} Message sent.'.format(emoji.worked))
            elif msg.channel.id == botdata.c.rx_vent:
                words = msg.content.split(' ')
                for i in words:
                    file = data.mclient['MAIN']['venting'].find_one({'tag' : i})
                    if file != None:
                        user = await client.fetch_user(int(file['user']))
                        await user.send('{} **{}**\n{}'.format(emoji.srt_right, msg.author, msg.content.replace(i, '')))
                        return await actions.say(msg.channel, '{} Message sent to user `{}`.'.format(emoji.worked, i))

            # SUGGESTIONS
            elif msg.channel.id == botdata.c.rx_suggestions or msg.channel.id == botdata.c.rxs_suggestions:
                h = await actions.say(msg.channel, '{}\n\n{} `Suggested by:` <@{}> ( {} ### {} )'.format(msg.content, emoji.srt_right, msg.author.id, msg.author, msg.author.id))
                await msg.delete()
                await h.add_reaction(emoji.upvote.replace('<', '').replace('>', ''))
                await h.add_reaction(emoji.downvote.replace('<', '').replace('>', ''))

            # WORD BY WORD STORY
            elif msg.channel.id == botdata.c.rx_story:
                if ' ' in msg.content or len(msg.content) > 15:
                    h = await actions.say(msg.channel, '{} You can only post 1 word at a time and it cannot be longer than 15 characters.'.format(emoji.error))
                    await msg.delete()
                    await asyncio.sleep(10)
                    await h.delete()
                else:
                    async for i in msg.channel.history(limit=data.limit):
                        if i.author.id == client.user.id:
                            await i.delete()
                            file = data.mclient['MAIN']['stories'].find_one({'currentstory' : '.'})
                            return await actions.say(msg.channel, '{} The topic of the story is: `{}`'.format(emoji.srt_right, file['topic']))

            # INTRODUCTIONS
            elif msg.channel.id == botdata.c.rx_intros:
                overwrite = discord.PermissionOverwrite()
                overwrite.send_messages = False
                await msg.channel.set_permissions(msg.author, overwrite=overwrite)

            # PARTNERSHIP MESSAGE & COUNT
            elif msg.channel.id == botdata.c.rx_partners:
                file = data.mclient['MAIN']['partnerships'].find_one({'user' : str(msg.author.id)})
                if file == None:
                    data.mclient['MAIN']['partnerships'].insert_one({'user' : str(msg.author.id), 'partnerships' : 1})
                else:
                    data.mclient['MAIN']['partnerships'].update_one({'user' : str(msg.author.id)}, {'$set' : {'partnerships' : int(file['partnerships']) + 1}})
                async for i in msg.channel.history():
                    if i.author.id == client.user.id:
                        await i.delete()
                        break
                await actions.say(msg.channel, '{} To partner please DM a <@&{}>.\n{} We partner with any server!'.format(emoji.srt_right, botdata.r.rx_pms, emoji.srt_right))

            # ACTIVITY COUNT
            elif msg.channel.id == botdata.c.rx_general and not msg.author.id == 578486764520603648:
                file = data.mclient['MAIN']['messages'].find_one({'user' : str(msg.author.id)})
                if file == None:
                    data.mclient['MAIN']['messages'].insert_one({'user' : str(msg.author.id), 'messages' : 1})
                else:
                    data.mclient['MAIN']['messages'].update_one({'user' : str(msg.author.id)}, {'$set' : {'messages' : int(file['messages']) + 1}})
                counter.append(0)
                a = len(counter)
                await asyncio.sleep(600)
                if len(counter) == a:
                    h = await actions.say(msg.channel, '{} Feel free to mention the <@&602138222864105473> if you wanna revive the chat!\n__Use `xg!roleme Activity` in <#594444988004433930> to get or remove the role.__'.format(emoji.srt_right))
                    counter.clear()
                    await asyncio.sleep(300)
                    await h.delete()
                    
        elif msg.channel.id == botdata.c.rx_general and msg.author.id != client.user.id:
            await asyncio.sleep(60)
            await msg.delete()

def setup(client):
    client.add_cog(MessageSystems(client))
