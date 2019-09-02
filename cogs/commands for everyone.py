import discord
from discord.ext import commands
import botdata
import time
import actions

data = botdata.d
emoji = botdata.e
client = data.client
color = data.color
cmds = data.cmds
cmds_numbers = {'1' : 'everyone',
                '2' : 'partner managers',
                '3' : 'e/g managers',
                '4' : 'helpers',
                '5' : 'moderators',
                '6' : 'administrators',
                '7' : 'managers',
                '8' : 'owners',
                '9' : 'bot staff'}

class CommandsForEveryone(commands.Cog):
    def __init__(self, client):
        self.client = client

    # help [command/number]
    @commands.command(aliases=['h'])
    async def help(self, ctx, option = None):
        if option == None:
            m = '**List of commands:**\n'
            for i in cmds:
                m += '\n{} __Commands for {}:__ **({})**\n'.format(emoji.srt_right, cmds_numbers[i], i)
                for u in cmds[i]:
                    m += '`{}` | '.format(u)
            await actions.say(ctx.message.channel, m)
        else:
            try:
                test = int(option)
                if option not in cmds_numbers:
                    await actions.say(ctx.message.channel, '{} Invalid category number given.'.format(emoji.error))
                else:
                    m = '**List of commands for {}:**\n\n```md'.format(cmds_numbers[option])
                    for i in cmds[option]:
                        m += '\n> {}\n# {}'.format(cmds[option][i][2].replace('p?', data.prefix), cmds[option][i][1])
                    m += '\n```'
                    await actions.say(ctx.message.channel, m)
            except:
                for i in cmds:
                    for u in cmds[i]:
                        if option.lower() == u or option.lower() in cmds[i][u][0]:
                            m = ':label: `Command:` {}'.format(u)
                            m += '\n:clipboard: `Description:` {}'.format(cmds[i][u][1])
                            m += '\n:wrench: `Usage:` {}'.format(cmds[i][u][2].replace('p?', data.prefix))
                            m += '\n:link: `Aliases:`'
                            if len(u[0]) != 0:
                                for o in cmds[i][u][0]:
                                     m += ' {}{}'.format(data.prefix, o)
                            else:
                                m += ' /'
                            m += '\n:book: `Examples:`\n{}'.format(cmds[i][u][3].replace('p?', data.prefix))
                            return await actions.say(ctx.message.channel, m)
                await actions.say(ctx.message.channel, '{} Invalid command given.'.format(emoji.error))

    # ping
    @commands.command()
    async def ping(self, ctx):
        t1 = time.time()
        await ctx.trigger_typing()
        response = round((time.time() - t1), 2)
        ping = round(client.latency, 2)
        m = ':satellite: Ping: `{} seconds`.'.format(ping)
        if ping <= 50:
            m += '\n{} The bot isn\'t lagging.'.format(emoji.ping_good)
        elif ping <= 100:
            m += '\n{} The bot might be lagging.'.format(emoji.ping_okay)
        elif ping > 100:
            m += '\n{} The bot is lagging.'.format(emoji.ping_bad)
        m += '\n:stopwatch:Response time: `{} seconds`.'.format(response)
        await actions.say(ctx.message.channel, m)

    # invite
    @commands.command(aliases=['inv'])
    async def invite(self, ctx):
        m = '{} **Community server:**'.format(emoji.srt_right)
        m += '\n[Click here]({}) to join.'.format(data.community[1])
        m += '\n{} **Support server:**'.format(emoji.srt_right)
        m += '\n[Click here]({}) to join.'.format(data.support[1])
        m += '\n'
        m += '\n{} [Click here](https://discordapp.com/oauth2/authorize?client_id=592762564186996761&scope=bot&permissions=8) to invite X Protection.'.format(emoji.plogo)
        m += '\n{} [Click here](https://discordapp.com/oauth2/authorize?client_id=578500711604813824&scope=bot&permissions=8) to invite X Moderation.'.format(emoji.mlogo)
        m += '\n{} [Click here](https://discordapp.com/oauth2/authorize?client_id=578500578653503498&scope=bot&permissions=8) to invite X General.'.format(emoji.glogo)
        m += '\n{} X Fun is not public yet.'.format(emoji.flogo)
        m += '\n{} X Advertisement is not public yet.'.format(emoji.alogo)
        m += '\n'
        m += '\n{} This bot is private and you cannot invite it to your server.'.format(emoji.rlogo)
        await actions.say(ctx.message.channel, m)

    # community
    @commands.command(aliases=['com'])
    async def community(self, ctx):
        await actions.say(ctx.message.channel, ':link: [Click here]({}) to join the community server.'.format(data.community[1]))

    # support
    @commands.command(aliases=['sup'])
    async def support(self, ctx):
        await actions.say(ctx.message.channel, ':link: [Click here]({}) to join the X bots support server.'.format(data.support[1]))

    # tos
    @commands.command()
    async def tos(self, ctx):
        m = await client.get_channel(botdata.c.rx_rules).fetch_message(data.tos)
        await actions.say(ctx.message.channel, m.content)

    # rules
    @commands.command()
    async def rules(self, ctx):
        if ctx.message.guild.id == int(data.community[0]):
            m = await client.get_channel(botdata.c.rx_rules).fetch_message(data.rx_rules)
        else:
            m = await client.get_channel(botdata.c.rxs_rules).fetch_message(data.rxs_rules)
        await actions.say(ctx.message.channel, m.content)

    # story <option> [text]
    @commands.command()
    async def story(self, ctx, option = None, *, text = None):
        if option == None:
            await actions.say(ctx.message.channel, '{} No option given.\n{} To see a list of stories use `{}story list`.\n{} To start a new story use `{}story topic <new topic>`.'.format(emoji.error, emoji.srt_right, data.prefix, emoji.srt_right, data.prefix))
        elif option.lower() == 'list':
            m = '{} **List of stories:**'.format(emoji.srt_right)
            m += '\n'
            a = ''
            for i in data.mclient['MAIN']['stories'].find():
                a += '\n`-` {}'.format(i['topic'])
            if a == '':
                m += '\nNo stories found.'
            else:
                m += a
            m += '\n'
            m += '\n{} To select a story use `{}story select <topic>`.'.format(emoji.srt_right, data.prefix)
            await actions.say(ctx.message.channel, m)
        elif option.lower() == 'topic':
            f = await actions.permission_check(ctx, 'HELPER')
            if f == True:
                if text == None:
                    await actions.say(ctx.message.channel, '{} No topic given.'.format(emoji.error))
                elif len(text) > 50:
                    await actions.say(ctx.message.channel, '{} The topic cannot be longer than 50 characters.'.format(emoji.error))
                else:
                    current = data.mclient['MAIN']['stories'].find_one({'currentstory' : '.'})
                    h = await actions.say(ctx.message.channel, '{} Saving current story...'.format(emoji.loading_circle))
                    words = []
                    async for i in client.get_channel(botdata.c.rx_story).history(limit=data.limit):
                        if len(i.attachments) == 0 and not i.pinned and not i.author.bot:
                            words.append(i.content)
                            await i.delete()
                    words.reverse()
                    m = ''
                    for i in words:
                        m += '{} '.format(i)
                    data.mclient['MAIN']['stories'].insert_one({'topic' : current['topic'], 'story' : m})
                    await actions.edit(h, '{} Current story saved with topic `{}`.\n{} Starting new story...'.format(emoji.worked, current['topic'], emoji.loading_circle))
                    data.mclient['MAIN']['stories'].update_one({'currentstory' : '.'}, {'$set' : {'topic' : text}})
                    await actions.say(client.get_channel(botdata.c.rx_story), '{} **__NEW STORY TOPIC:__**\n\n{}'.format(emoji.srt_right, text))
                    await actions.edit(h, '{} New story started.'.format(emoji.worked))
                    l = '{} **New story started:**'.format(emoji.log)
                    l += '\n'
                    l += '\n{} `Started by:` <@{}> ( {} ### {} )'.format(emoji.srt_right, ctx.message.author.id, ctx.message.author, ctx.message.author.id)
                    l += '\n{} `Topic:` {}'.format(emoji.srt_right, text)
                    await actions.send_log(ctx.message, l)
        elif option.lower() == 'select':
            file = data.mclient['MAIN']['stories'].find_one({'topic' : text})
            if file == None:
                await actions.say(ctx.message.channel, '{} Topic not found.'.format(emoji.error))
            else:
                h = await actions.say(ctx.message.channel, '{} The story will be DMed to you.'.format(emoji.srt_right))
                m = '{} **{}:**'.format(emoji.srt_right, text)
                a = []
                try:
                    words = file['story'].split(' ')
                    for i in words:
                        m += ' {}'.format(i)
                        a.append('0')
                        if len(m) > 1900 or len(a) == len(words):
                            try:
                                await ctx.message.author.send(m)
                                m = ''
                            except:
                                await actions.edit(h, '{} Unable to DM you.\n{} Please enable DMs and try again.'.format(emoji.error, emoji.srt_right))
                                break
                except:
                    words = []
                    async for i in client.get_channel(botdata.c.rx_story).history(limit=data.limit):
                        if len(i.attachments) == 0and not i.pinned and not i.author.bot:
                            words.append(i.content)
                    words.reverse()
                    for i in words:
                        m += '{} '.format(i)
                        a.append('0')
                        if len(m) > 1900 or len(a) == len(words):
                            try:
                                await ctx.message.author.send(m)
                                m = ''
                            except:
                                await actions.edit(h, '{} Unable to DM you.\n{} Please enable DMs and try again.'.format(emoji.error, emoji.srt_right))
                                break
        else:
            await actions.say(ctx.message.channel, '{} No option given.\n{} To see a list of stories use `{}story list`.\n{} To start a new story use `{}story topic <new topic>`.'.format(emoji.error, emoji.srt_right, data.prefix, emoji.srt_right, data.prefix))

    # bump
    @commands.command()
    async def bump(self, ctx):
        m = '{} **Bumping information:**'.format(emoji.srt_right)
        m += '\nBumping is a way of advertising the server on server lists.'
        m += '\nBy bumping the server you\'re helping it grow!'
        m += '\n'
        m += '\n{} `Bump links & commands:`'.format(emoji.srt_right)
        m += '\n**>>** !d bump'
        m += '\n**>>** |bump'
        m += '\n**>>** [Click here](https://disboard.org/review/create/579385116443541526) to post a review for Realm X.'
        m += '\n**>>** [Click here](https://disboard.org/review/create/598936343350870029) to post a review for Realm X Support.'
        await actions.say(ctx.message.channel, m)

    # pm
    @commands.command()
    async def pm(self, ctx):
        m = '**Partnership message:**'
        m += '\n`**⎯⎯Realm X⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯**'
        m += '\n'
        m += '\n:small_red_triangle_down: A place where all misfits and outcasts can get together and hang out, make friends and just have a great time.'
        m += '\n:small_red_triangle: It\'s the perfect place for anyone who\'s feeling left out, rejected, alone or is unable to fit in.'
        m += '\n'
        m += '\n```yaml'
        m += '\n    ⎯⎯Active chats⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯'
        m += '\n    ⎯⎯Interesting, unique and friendly people⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯'
        m += '\n    ⎯⎯Chill community and staff⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯'
        m += '\n    ⎯⎯Events and giveaways⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯'
        m += '\n    ⎯⎯Fun channels⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯'
        m += '\n    ⎯⎯Custom bots⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯'
        m += '\n```'
        m += '\n'
        m += '\n**Join us now! Don\'t take too long, we are waiting for you!**'
        m += '\n'
        m += '\n:link: https://discord.gg/53mGEpb'
        m += '\n:frame_photo: https://i.imgur.com/uIn8mmU.png'
        m += '\n:bell: @everyone @here`'
        await actions.say(ctx.message.channel, m)

    # mc [option] [text/user]
    @commands.command()
    async def mc(self, ctx, option = None):
        if option == None:
            m = '**Minecraft SMP server information:**'
            m += '\n'
            m += '\n{} `Description:` This is a Minecraft survival multiplayer server where Realm X members can hang out and have fun.'.format(emoji.srt_right)
            m += '\n'
            m += '\n{} `IP:` RealmX.mcnetwork.me'.format(emoji.srt_right)
            m += '\n{} `Version:` 1.14.4'.format(emoji.srt_right)
            m += '\n{} `Type:` cracked'.format(emoji.srt_right)
            m += '\n{} `Operators:`'.format(emoji.srt_right)
            for i in ctx.message.guild.get_role(botdata.r.rx_mc_op).members:
                m += ' <@{}>'.format(i.id)
            m += '\n'
            m += '\n{} If the server is about to expire please use `{}mc renew`.'.format(emoji.srt_right, data.prefix)
            m += '\n'
            m += '\n{} **Notes:**'.format(emoji.srt_right)
            m += '\n`-` The server is cracked and secured with a login plugin.'
            m += '\n`-` The server is not 24/7 due to the renewing system for free servers on the hosting site.'
            await actions.say(ctx.message.channel, m)
        elif option.lower() == 'renew':
            h = await actions.say(ctx.message.channel, '{} Sending notifications to the server operators...'.format(emoji.loading_circle))
            for i in ctx.message.guild.get_role(botdata.r.rx_mc_op).members:
                try:
                    await actions.say(i, '{} **The Minecraft server needs to be renewed!**\n{} `Link:` [Please remind me to set this link ~ Zero](https://omfgdogs.com/)\n\n{} `Renew requested by:` <@{}> ( {} ### {} )'.format(emoji.error, emoji.server, emoji.srt_right, ctx.message.author.id, ctx.message.author, ctx.message.author.id))
                except:
                    pass
            await actions.edit(h, '{} All server operators have been notified to renew the server.'.format(emoji.worked))
        else:
            await actions.say(ctx.message.channel, '{} Invalid option given.\n{} Use `{}mc` for more information.'.format(emoji.error, emoji.srt_right, data.prefix))

    # messages [user]
    @commands.command(aliases=['msgs'])
    async def messages(self, ctx, user: discord.Member = None):
        if user != None:
            file = data.mclient['MAIN']['messages'].find_one({'user' : str(user.id)})
            if file == None:
                await actions.say(ctx.message.channel, '{} That user hasn\'t sent any messages in <#{}> this week.'.format(emoji.error, botdata.c.rx_general))
            else:
                await actions.say(ctx.message.channel, '{} <@{}> has sent sent **{}** message(s) in <#{}> this week.'.format(emoji.srt_right, user.id, file['messages'], botdata.c.rx_general))
        else:
            h = await actions.say(ctx.message.channel, '{} Loading activity leaderboard...'.format(emoji.loading_circle))
            sent = []
            users = {}
            for i in data.mclient['MAIN']['messages'].find():
                sent.append(int(i['messages']))
                users[i['user']] = str(i['messages'])
            sent.sort()
            sent.reverse()
            m = '{} **Activity leaderboard:**'.format(emoji.srt_right)
            m += '\n'
            b = {'1' : ':crown:',
                 '2' : ':trophy:',
                 '3' : ':trident:',
                 '4' : ':medal:',
                 '5' : ':beginner:',
                 '6' : ':beginner:',
                 '7' : ':beginner:',
                 '8' : ':beginner:',
                 '9' : ':beginner:',
                 '10' : ':beginner:'}
            n = 0
            e = ''
            total = 0
            people = 0
            for i in sent:
                for u in users:
                    if users[u] == str(i):
                        person = u
                        break
                n += 1
                if str(n) in b:
                    m += '\n{} <@{}> `-` **{}** message(s)'.format(b[str(n)], person, i)
                    total += int(i)
                    people += 1
                if person == str(ctx.message.author.id):
                    e += '{} <@{}> `-` **{}** message(s)'.format(emoji.srt_right, ctx.message.author.id, i)
                del users[person]
            m += '\n'
            m += '\n{}'.format(e)
            m += '\n{} Total: **{}** messages.'.format(emoji.srt_right, total)
            m += '\n{} Average: **{}** messages.'.format(emoji.srt_right, int(total / people))
            await actions.edit(h, m)

    # partnerships [user]
    @commands.command(aliases=['partners'])
    async def partnerships(self, ctx, user: discord.Member = None):
        if user != None:
            file = data.mclient['MAIN']['partnerships'].find_one({'user' : str(user.id)})
            if file == None:
                await actions.say(ctx.message.channel, '{} That user hasn\'t made any partnerships this week.'.format(emoji.error))
            else:
                await actions.say(ctx.message.channel, '{] <@{}> has made **{}** partnership(s) this week.'.format(emoji.srt_right, user.id, file['partnerships']))
        else:
            h = await actions.say(ctx.message.channel, '{} Loading partnerships leaderboard...'.format(emoji.loading_circle))
            sent = []
            users = {}
            for i in data.mclient['MAIN']['partnerships'].find():
                sent.append(int(i['partnerships']))
                users[i['user']] = str(i['partnerships'])
            sent.sort()
            sent.reverse()
            m = '{} **Partnerships leaderboard:**'.format(emoji.srt_right)
            m += '\n'
            b = {'1' : ':crown:',
                 '2' : ':trophy:',
                 '3' : ':trident:',
                 '4' : ':medal:',
                 '5' : ':beginner:',
                 '6' : ':beginner:',
                 '7' : ':beginner:',
                 '8' : ':beginner:',
                 '9' : ':beginner:',
                 '10' : ':beginner:'}
            n = 0
            e = ''
            for i in sent:
                for u in users:
                    if users[u] == str(i):
                        person = u
                        break
                n += 1
                if str(n) in b:
                    m += '\n{} <@{}> `-` **{}** partnership(s)'.format(b[str(n)], person, i)
                if person == str(ctx.message.author.id):
                    e += '{} <@{}> `-` **{}** partnership(s)'.format(emoji.srt_right, ctx.message.author.id, i)
                if n == 10 and e != '':
                    break
                del users[person]
            m += '\n'
            m += '\n{}'.format(e)
            await actions.edit(h, m)
            
    # upvotes [user]
    @commands.command(aliases=['uvs'])
    async def upvotes(self, ctx, user: discord.Member = None):
        if user != None:
            file = data.mclient['MAIN']['upvotes'].find_one({'user' : str(user.id)})
            if file == None:
                await actions.say(ctx.message.channel, '{} That user hasn\'t gotten upvotes this week.'.format(emoji.error))
            else:
                await actions.say(ctx.message.channel, '{] <@{}> has **{}** upvote(s) this week.'.format(emoji.srt_right, user.id, file['upvotes']))
        else:
            h = await actions.say(ctx.message.channel, '{} Loading upvotes leaderboard...'.format(emoji.loading_circle))
            sent = []
            users = {}
            for i in data.mclient['MAIN']['upvotes'].find():
                sent.append(int(i['upvotes']))
                users[i['user']] = str(i['upvotes'])
            sent.sort()
            sent.reverse()
            m = '{} **Upvotes leaderboard:**'.format(emoji.srt_right)
            m += '\n'
            b = {'1' : ':crown:',
                 '2' : ':trophy:',
                 '3' : ':trident:',
                 '4' : ':medal:',
                 '5' : ':beginner:',
                 '6' : ':beginner:',
                 '7' : ':beginner:',
                 '8' : ':beginner:',
                 '9' : ':beginner:',
                 '10' : ':beginner:'}
            n = 0
            e = ''
            for i in sent:
                for u in users:
                    if users[u] == str(i):
                        person = u
                        break
                n += 1
                if str(n) in b:
                    m += '\n{} <@{}> `-` **{}** upvote(s)'.format(b[str(n)], person, i)
                if person == str(ctx.message.author.id):
                    e += '{} <@{}> `-` **{}** upvote(s)'.format(emoji.srt_right, ctx.message.author.id, i)
                if n == 10 and e != '':
                    break
                del users[person]
            m += '\n'
            m += '\n{}'.format(e)
            await actions.edit(h, m)


def setup(client):
    client.remove_command('help')
    client.add_cog(CommandsForEveryone(client))
