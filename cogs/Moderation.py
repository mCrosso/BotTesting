import random

from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def purge(self, ctx, amount=100):
        if ctx.author == self.client:
            return
        await ctx.message.delete(delay=None)
        await ctx.channel.purge(limit=amount)

def setup(client):
    client.add_cog(Moderation(client))
