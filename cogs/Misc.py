import random
import discord

import datetime

from discord.ext import commands


class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def av(self, ctx, user: discord.User = None):
        user = ctx.author if not user else user
        embed = discord.Embed(
            description='Avatar,',
            color=0xecce8b)
        pfp = user.avatar_url
        embed.set_author(name=user.name, icon_url=ctx.author.avatar_url)
        embed.set_image(url=pfp)
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        global deletedmessage
        deletedmessage = message.content
    @commands.command()
    async def snipe(self, ctx):
        colors = [0xFF0000, 0x000000, 0x0000FF, 0x008000, 0xFFFF00, 0xFFA500, 0x800080]
        randomchoice = random.choice(colors)
        user = ctx.author
        embed = discord.Embed(
            description=deletedmessage,
            timestamp=(datetime.datetime.utcnow()),
            color=randomchoice)
        embed.set_author(name=user.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    @snipe.error
    async def on_error(self, ctx, error):
        await ctx.send("There's nothing to snipe!")

    @commands.command()
    async def id(self, ctx, user: discord.User = None):
        user = ctx.author if not user else user
        embed = discord.Embed(
            description=f'ID is: {user.id}')
        embed.set_author(name="User's ID", icon_url=user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! Ping is {round(self.client.latency * 1000)}ms")


def setup(client):
    client.add_cog(Misc(client))
