import random
import discord

from discord.ext import commands


class Funcommands(commands.Cog, name='Fun commands'):

    def __init__(self, client):
        self.client = client

    @commands.command(name='8ball')
    async def _8ball(self, ctx):
        responses = ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes – definitely.',
                     'You may rely on it.', 'As I see it, yes.', 'Most likely.',
                     'Outlook good.', 'Yes.', 'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.',
                     'Better not tell you now.', 'Cannot predict now.',
                     'Concentrate and ask again.', "Don't count on it.", 'My reply is no.', 'My sources say no.',
                     'Outlook not so good.', 'Very doubtful.']
        await ctx.send(random.choice(responses))


    @commands.command()
    async def isbuttergay(self, ctx):
        await ctx.send('OFC SHE IS')

    @commands.command()
    async def say(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send(message)
    @commands.command()
    async def ship(self, ctx, user1, *, user2=None):
        if user2 is None:
            user2 = user1
            user1 = ctx.author.name

        randval = random.randint(0, 100)
        emotesnum = int(str(round(randval / 10)))
        rest = 10 - emotesnum
        global possibs
        possibs = ''
        if randval <= 10:
            possibs = "Awful"
        elif 10 <= randval < 20:
            possibs = "Bad"
        elif 20 <= randval < 30:
            possibs = "Not too good"
        elif 30 <= randval < 50:
            possibs = 'Below average'
        elif randval == 50:
            possibs = 'Meh'
        elif 50 <= randval < 60:
            possibs = 'Not bad'
        elif 60 <= randval < 70:
            possibs = 'Good'
        elif 70 <= randval < 80:
            possibs = "Very good"
        elif 80 <= randval < 90:
            possibs = "Amazing"
        elif 90 <= randval <= 100:
            possibs = 'Perfect'
        black = '<:NewProject1:725706978193702933>'
        purple = '<:purple:725706951425785948>'
        embed = discord.Embed(
            title=":heartbeat: **MATCHMAKING** :heartbeat:",
            description=(
                f':arrow_down_small: {user1} \n :arrow_up_small:  {user2} \n \n **{randval}%** {emotesnum * purple}{black * rest} {possibs}'),
            color=0xff00a2)
        await ctx.send(embed=embed)
    @commands.command(name='8ball2', Aliases=['8ball2'])
    async def _8ball2(self, ctx):
        randval = random.randint(0, 100)
        emotesnum = int(str(round(randval / 10)))
        black = '<:NewProject1:725706978193702933>'
        purple = '<:purple:725706951425785948>'
        rest = 10 - emotesnum
        global possibs
        possibs = ''
        if randval <= 10:
            possibs = "Nope, never"
        elif 10 <= randval < 20:
            possibs = "I doubt that"
        elif 20 <= randval < 30:
            possibs = "Small chance"
        elif 30 <= randval < 50:
            possibs = 'Below average'
        elif randval == 50:
            possibs = 'Meh'
        elif 50 <= randval < 60:
            possibs = 'Maybe'
        elif 60 <= randval < 70:
            possibs = 'Yes by a small chance'
        elif 70 <= randval < 80:
            possibs = "Of course"
        elif 80 <= randval < 90:
            possibs = "Obviously"
        elif 90 <= randval <= 100:
            possibs = 'HELL YEAH'
        embed = discord.Embed(
            description=f'{randval}% True ** {emotesnum * purple}{black * rest} {possibs} ** ',
            color=0x000000)
        embed.set_author(name=f'Truth Machine', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Funcommands(client))
