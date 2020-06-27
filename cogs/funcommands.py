import discord
from discord.ext import commands
class Funcommands(commands.Cog):

    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot working!')
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('test')
def setup(client):
    client.add_cog(Funcommands(client))
