import discord
from discord.ext import commands
import botdata
import time
import asyncio

data = botdata.d
emoji = botdata.e
channel = botdata.c
client = data.client
color = data.color

# SAY
async def say(target, message, content = None):
    embed = discord.Embed(colour=color)
    try:
        if target.guild.id == str(data.community[0]):
            embed.set_footer(text='>> {}'.format(data.support[1]))
        else:
            embed.set_footer(text='>> {}'.format(data.community[1]))
    except:
        embed.set_footer(text='>> {}'.format(data.community[1]))
    embed.description = message
    if content == None:
        return await target.send(embed=embed)
    else:
        return await target.send(content=content, embed=embed)

# EDIT
async def edit(target, message, content = None):
    embed = discord.Embed(colour=color)
    try:
        if target.guild.id == str(data.community[0]):
            embed.set_footer(text='>> {}'.format(data.support[1]))
        else:
            embed.set_footer(text='>> {}'.format(data.community[1]))
    except:
        embed.set_footer(text='>> {}'.format(data.community[1]))
    embed.description = message
    if content == None:
        return await target.edit(embed=embed)
    else:
        return await target.edit(content=content, embed=embed)

# PERMISSION CHECK
async def permission_check(ctx, role):
    if ctx.message.author.guild_permissions.administrator == True:
        return True
    if ctx.message.guild.id == int(data.community[0]):
        perms = {'OWNER' : [botdata.r.rx_owners],
                 'MANAGER' : [botdata.r.rx_owners, botdata.r.rx_managers],
                 'ADMIN' : [botdata.r.rx_owners, botdata.r.rx_managers, botdata.r.rx_admins],
                 'MOD' : [botdata.r.rx_owners, botdata.r.rx_managers, botdata.r.rx_admins, botdata.r.rx_mods],
                 'HELPER' : [botdata.r.rx_owners, botdata.r.rx_managers, botdata.r.rx_admins, botdata.r.rx_mods, botdata.r.rx_helpers],
                 'EG' : [botdata.r.rx_owners, botdata.r.rx_managers, botdata.r.rx_admins, botdata.r.rx_mods, botdata.r.rx_helpers, botdata.r.rx_egs],
                 'PM' : [botdata.r.rx_owners, botdata.r.rx_managers, botdata.r.rx_admins, botdata.r.rx_mods, botdata.r.rx_helpers, botdata.r.rx_egs, botdata.r.rx_pms]}
    elif ctx.message.guild.id == int(data.support[0]):
        perms = {'OWNER' : [botdata.r.rxs_owner],
                 'BOT STAFF' : [botdata.r.rxs_owner, botdata.r.rxs_staff]}
    for i in perms[role]:
        if ctx.message.guild.get_role(i) in ctx.message.author.roles:
            return True
    await say(ctx.message.channel, '{} You do not have permission to use this command.'.format(emoji.no_perms))

# SEND LOG
async def send_log(msg, message):
    if msg.guild.id == int(data.community[0]):
        await say(client.get_channel(channel.rx_logs), message)
    else:
        await say(client.get_channel(channel.rxs_logs), message)
