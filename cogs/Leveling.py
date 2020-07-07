import random
import sqlite3

import discord
from discord.ext import commands

import math

# noinspection PyShadowingNames,PyUnusedLocal
class Leveling(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_message(self, message):
        db = sqlite3.connect('lvls.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT user_id FROM lvls WHERE guild_id = '{message.guild.id}' and user_id = '{message.author.id}'")
        result = cursor.fetchone()
        if result is None:
            # noinspection PyRedundantParentheses
            sql = ("INSERT INTO lvls(guild_id, user_id, exp, lvl) VALUES(?, ?, ?, ?)")
            val = (message.guild.id, message.author.id, 2, 0)
            cursor.execute(sql, val)
            db.commit()

        else:
            cursor.execute(f"SELECT user_id, exp, lvl FROM lvls WHERE guild_id = '{message.guild.id}' and user_id = '{message.author.id}'")
            result1 = cursor.fetchone()
            exp = int(result1[1])
            sql = (f"UPDATE lvls SET exp = ({exp + 2}) WHERE guild_id = ({str(message.guild.id)}) and user_id = ({str(message.author.id)})")
            cursor.execute(sql)
            db.commit()

            cursor.execute(
                f"SELECT user_id, exp, lvl FROM lvls WHERE guild_id = '{message.guild.id}' and user_id = '{message.author.id}'")
            result2 = cursor.fetchone()

            xp_start = int(result2[1])
            lvl_start = int(result2[2])
            xp_end = math.floor(5 * (lvl_start ** 2) * 2 + 50 * lvl_start + 100)
            if xp_end < xp_start:
                await message.channel.send(f'{message.author.mention} has leveled up to level {lvl_start + 1}.')
                sql = (f"UPDATE lvls SET lvl = ? WHERE guild_id = ? and user_id = ?")
                val = (lvl_start + 1, str(message.guild.id), str(message.author.id))
                cursor.execute(sql, val)
                db.commit()
                sql = (f"UPDATE lvls SET exp = ? WHERE guild_id = ? and user_id = ?")
                val = (0, str(message.guild.id), str(message.author.id))
                cursor.execute(sql, val)
                db.commit()
                cursor.close()
                db.close()
    @commands.command()
    async def rank(self, ctx, user: discord.User = None):
        if user is None:
            user = ctx.author
        db = sqlite3.connect('lvls.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT lvl FROM lvls WHERE guild_id = {ctx.message.guild.id} and user_id = {user.id}")
        result = cursor.fetchone()
        cursor.execute(f"SELECT exp FROM lvls WHERE guild_id = {ctx.message.guild.id} and user_id = {user.id}")
        result2 = cursor.fetchone()
        embed = discord.Embed(
            description=f"{user.name}'s level is {result[0]} and has {result2[0]} exp.",
            color=0xecce8b)
        pfp = user.avatar_url
        embed.set_author(name=user.name, icon_url=user.avatar_url)
        await ctx.send(embed=embed)















def setup(client):
    client.add_cog(Leveling(client))
