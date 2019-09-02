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
r = botdata.r

class JoinLeaveSystems(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, user):
        # WELCOME AND JOIN LOGS
        if user.guild.id == int(data.community[0]):
            await client.get_channel(botdata.c.rx_general).send(':wave: **Welcome,** <@{}>**, to the server!\nWe hope you enjoy your stay!**'.format(user.id))
            await client.get_channel(botdata.c.rx_guestbook).send('{} `{}` joined the server. We now have **{}** members!'.format(emoji.support, user, len(user.guild.members)))
            m = ':wave: **Hello! Welcome to Realm X**!'
            m += '\n'
            m += '\n{} Use `xg!roleme` in <#594444988004433930> to get roles.'.format(emoji.srt_right)
            m += '\n{} We partner with any server so feel free to contact a partner manager if you\'re looking to partner!'.format(emoji.srt_right)
            m += '\n{} We also have a Minecraft 1.14.4 SMP server: `RealmX.mcnetwork.me`'.format(emoji.srt_right)
            m += '\n'
            m += '\n__We\'re happy to have you here, hope you enjoy your stay!__'
            await user.send(m)
        elif user.guild.id == int(data.support[0]):
            await client.get_channel(botdata.c.rxs_general).send(':wave: **Welcome,** <@{}>**, to the server!\nWe hope you enjoy your stay!**'.format(user.id))
            await client.get_channel(botdata.c.rxs_guestbook).send('{} `{}` joined the server. We now have **{}** members!'.format(emoji.support, user, len(user.guild.members)))

    @commands.Cog.listener()
    async def on_member_remove(self, user):
        # LEAVE LOGS
        if user.guild.id == int(data.community[0]):
            await client.get_channel(botdata.c.rx_guestbook).send('{} `{}` left the server. We now have **{}** members!'.format(emoji.minus, user, len(user.guild.members)))
        elif user.guild.id == int(data.support[0]):
            await client.get_channel(botdata.c.rxs_guestbook).send('{} `{}` left the server. We now have **{}** members!'.format(emoji.minus, user, len(user.guild.members)))

def setup(client):
    client.add_cog(JoinLeaveSystems(client))
