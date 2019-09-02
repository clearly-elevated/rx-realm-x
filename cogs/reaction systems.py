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

class ReactionSystems(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        # STAR BOARD
        if payload.guild_id == int(data.community[0]) and payload.channel_id == botdata.c.rx_general:
            channel = client.get_channel(payload.channel_id)
            msg = await channel.fetch_message(payload.message_id)
            user = await client.fetch_user(msg.author.id)
            if not user.bot:
                for i in msg.reactions:
                    if str(i.emoji) == '⭐':
                        if i.count == 1:
                            embed = discord.Embed(colour=data.color)
                            embed.set_footer(text='>> {}'.format(data.community[1]))
                            embed.description = '{}\n{}*~ <@{}>*'.format(msg.content, emoji.blank, user.id)
                            if len(msg.attachments) > 0:
                                embed.set_image(url=msg.attachments[0].url)
                            return await client.get_channel(botdata.c.rx_quotes).send(embed=embed)
                        else:
                            break

def setup(client):
    client.add_cog(ReactionSystems(client))
