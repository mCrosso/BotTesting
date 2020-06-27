import random
import discord

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


def setup(client):
    client.add_cog(Misc(client))
