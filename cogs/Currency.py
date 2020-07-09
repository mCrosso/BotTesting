import random
import sqlite3

import discord
from discord.ext import commands


# noinspection PyShadowingNames,PyUnusedLocal
class Currency(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, ctx):
        name = ctx.author
        name2 = f"'{name.id}'"
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        sql = (f'INSERT OR IGNORE INTO main (Username, Balance, Job, Jm)'
               f'VALUES(({name2}), (0), ("No job"), (0))')
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()

    @commands.command(aliases=['balance', 'Balance', 'Bal'])
    async def bal(self, ctx, member: discord.User = None):

        if member is None:
            member = ctx.author
            db = sqlite3.connect('main.sqlite')
            cursor = db.cursor()
            cursor.execute(f"SELECT Balance FROM main WHERE Username = '{member.id}'")
            result = cursor.fetchone()
            amount = str(result[0])
            embed = discord.Embed(
                description=f'You have {amount} coins.',
                color=0x000000)
            embed.set_author(name=f"{member.name}'s balance", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            db = sqlite3.connect('main.sqlite')
            cursor = db.cursor()
            cursor.execute(f"SELECT Balance FROM main WHERE Username = '{member.id}'")
            result = cursor.fetchone()
            amount = str(result[0])
            embed = discord.Embed(
                description=f'{member.name} has {amount} coins.',
                color=0x000000)
            embed.set_author(name=f"{member.name}'s balance", icon_url=member.avatar_url)
            await ctx.send(embed=embed)

    @bal.error
    async def on_error(self, ctx, error):
        await ctx.send("The mentioned user doesn't have an account")
    @commands.group()
    async def jobs(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(
                color=0x000000, )
            embed.add_field(name='Driver', value='Work as a Taxi Driver and get 20 coins per hour')
            embed.add_field(name='Developer', value='Work as a Developer and get 50 coins per hour')
            embed.add_field(name='Streamer', value='Work as a Streamer and get 100 coins per hour')
            await ctx.send(embed=embed)

    @jobs.error
    async def on_error(self, ctx, error):
        error1 = str(error).replace("You are on cooldown. Try again in ", '')
        error2 = str(error1).replace('s', '')
        error3 = round(float(float(error2) / 60))
        await ctx.send(f"You're on cooldown. Try again in {error3} minutes.")

    @jobs.command(aliases=['driver'])
    async def Driver(self, ctx):
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT Job FROM main WHERE Username = '{ctx.author.id}'")
        res = cursor.fetchone()
        if res[0] == 'Taxi Driver':
            await ctx.send("You're already a Taxi Driver.")
        else:
            sql = f"UPDATE main SET Job = 'Taxi Driver' WHERE Username = '{ctx.author.id}'"
            sql2 = f"UPDATE main SET Jm = 20 WHERE Username = '{ctx.author.id}'"
            cursor.execute(sql2)
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            await ctx.send(f"You're now working as a Taxi Driver!")

    @jobs.command(aliases=['Cam Girl', 'cam girl', 'camgirl', 'Camgirl', 'camGirl', 'cam', 'Cam'])
    async def CamGirl(self, ctx):
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT Username FROM main WHERE Username = '{ctx.author.id}'")
        res = cursor.fetchone()
        if res[0] != '638814602829889559':
            await ctx.send("You can't use this command.")
        else:
            cursor.execute(f"SELECT Job FROM main WHERE Username = '{ctx.author.id}'")
            res2 = cursor.fetchone()
            if res2[0] == 'Cam Girl':
                await ctx.send("You're already a Cam Girl")
            else:
                sql = f"UPDATE main SET Job = 'Cam Girl' WHERE Username = '{ctx.author.id}'"
                sql2 = f"UPDATE main SET Jm = 120 WHERE Username = '{ctx.author.id}'"
                cursor.execute(sql2)
                cursor.execute(sql)
                db.commit()
                cursor.close()
                db.close()
                await ctx.send(f"You're now working as a Cam Girl!")

    @jobs.command(aliases=['egirl', 'Egirl'])
    async def eGirl(self, ctx):
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT Username FROM main WHERE Username = '{ctx.author.id}'")
        res = cursor.fetchone()
        if res[0] != '361541867508334594':
            await ctx.send("You can't use this command.")
        else:
            cursor.execute(f"SELECT Job FROM main WHERE Username = '{ctx.author.id}'")
            res2 = cursor.fetchone()
            if res2[0] == 'eGirl':
                await ctx.send("You're already an eGirl")
            else:
                sql = f"UPDATE main SET Job = 'eGirl' WHERE Username = '{ctx.author.id}'"
                sql2 = f"UPDATE main SET Jm = 120 WHERE Username = '{ctx.author.id}'"
                cursor.execute(sql2)
                cursor.execute(sql)
                db.commit()
                cursor.close()
                db.close()
                await ctx.send(f"You're now an eGirl!")
    @jobs.command(aliases=['developer'])
    async def Developer(self, ctx):
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT Job FROM main WHERE Username = '{ctx.author.id}'")
        res = cursor.fetchone()
        if res[0] == 'Developer':
            await ctx.send("You're already a developer.")
        else:
            sql = f"UPDATE main SET Job = 'Developer' WHERE Username = '{ctx.author.id}'"
            sql2 = f"UPDATE main SET Jm = 50 WHERE Username = '{ctx.author.id}'"
            cursor.execute(sql2)
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            await ctx.send("You're now working as a Developer!")
    @jobs.command(aliases=['streamer'])
    async def Streamer(self, ctx):
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT Job FROM main WHERE Username = '{ctx.author.id}'")
        res = cursor.fetchone()
        if res[0] == 'Streamer':
            await ctx.send("You're already a streamer.")
        else:
            sql = f"UPDATE main SET Job = 'Streamer' WHERE Username = '{ctx.author.id}'"
            sql2 = f"UPDATE main SET Jm = 100 WHERE Username = '{ctx.author.id}'"
            cursor.execute(sql2)
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            await ctx.send("You're now working as a Streamer!")
    @commands.cooldown(1, 3594, commands.BucketType.user)
    @commands.command()
    async def work(self, ctx):
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT Job FROM main WHERE Username = '{ctx.author.id}'")
        result3 = cursor.fetchone()
        if result3[0] == 'None':
            await ctx.send("You don't have an job. You can choose a job by doing 'jobs' command.")
        else:
            cursor.execute(f"SELECT Jm FROM main WHERE Username = '{ctx.author.id}'")
            result = cursor.fetchone()
            await ctx.send(f'You worked for an hour and got {result[0]} coins!')
            global sql
            sql = f"UPDATE main SET Balance = (Balance + {result[0]}) WHERE Username = '{ctx.author.id}'"
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
    @work.error
    async def on_error(self, ctx, error):
        error1 = str(error).replace("You are on cooldown. Try again in ", '')
        error2 = str(error1).replace('s', '')
        error3 = round(float(float(error2) / 60))
        await ctx.send(f"You're on cooldown. Try again in {error3} minutes.")

    @commands.command()
    async def job(self, ctx):
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT Job FROM main WHERE Username = '{ctx.author.id}'")
        result = cursor.fetchone()
        if result[0] == 'No job':
            await ctx.send("You don't have an job. You can choose a job by doing 'jobs' command.")
        else:
            cursor.execute(f"SELECT Jm FROM main WHERE Username = '{ctx.author.id}'")
            result2 = cursor.fetchone()
            await ctx.send(f"You're working as a {result[0]} and you get {result2[0]} coins.")
    @commands.command()
    async def give(self, ctx, member: discord.User = None, *, amount=None):

        if member == None:
            await ctx.send('Please mention the user that you want to give money to.')
        elif amount is None:
            await ctx.send('Please type the amount of money you want to transfer.')
        else:
            db = sqlite3.connect('main.sqlite')
            cursor = db.cursor()
            cursor.execute(f"SELECT Balance FROM main WHERE Username = '{member.id}'")
            result2 = cursor.fetchone()
            if result2 is None:
                await ctx.send("The mentioned user doesn't have an account")
            else:
                cursor.execute(f"SELECT Balance FROM main WHERE Username = '{ctx.author.id}'")
                result = cursor.fetchone()
                if int(amount) > int(result[0]):
                    await ctx.send('The amount of money you want to send is bigger than yours.')
                else:
                    sql = f"UPDATE main SET Balance = (balance + {amount}) WHERE Username = '{member.id}'"
                    sql2 = f"UPDATE main SET Balance = (balance - {amount}) WHERE Username = '{ctx.author.id}'"
                    await ctx.send(f'You gave {member.name} {amount} coins.')

                    cursor.execute(sql)
                    cursor.execute(sql2)
                    db.commit()
                    cursor.close()
                    db.close()


def setup(client):
    client.add_cog(Currency(client))
