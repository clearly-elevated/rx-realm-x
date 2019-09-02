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

class EditMessageSystems(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_message_edit(self, payload):
        channel = client.get_channel(int(payload.data['channel_id']))
        msg = await channel.fetch_message(payload.message_id)
        if not msg.author.bot:
            # ANTI ONE WORD STORY BYPASS
            if channel.id == botdata.c.rx_story:
                if ' ' in msg.content or len(msg.content) > 15:
                    h = await actions.say(msg.channel, '{} You can only post 1 word at a time and it cannot be longer than 15 characters.'.format(emoji.error), content='<@{}>'.format(msg.author.id))
                    await asyncio.sleep(10)
                    await h.delete()

def setup(client):
    client.add_cog(EditMessageSystems(client))
