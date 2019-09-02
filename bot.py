import discord
from discord.ext import commands
import time
import botdata
import actions
import os

t1 = time.time()
data = botdata.d
emoji = botdata.e
color = data.color
client = data.client

for i in data.extensions:
    client.load_extension(i)

# START UP
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='with your dreams...'.format(data.prefix, data.prefix, data.prefix)))
    m = '{} **__Bot Started__** {}'.format(emoji.log, emoji.reload)
    m += '\n'
    m += '\n{} `Version:` {}'.format(emoji.worked, data.version)
    m += '\n{} `Ping:` {} seconds'.format(emoji.ping_okay, round(client.latency, 2))
    m += '\n{} `Time taken:` {} seconds'.format(emoji.srt_right, round(time.time() - t1, 2))
    h = await actions.say(client.get_channel(botdata.c.rxs_logs), m)
    print('Started!')

# RUN
client.run(os.environ['BOT_TOKEN'])

