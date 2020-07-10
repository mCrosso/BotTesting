import random
from PIL import Image, ImageFont, ImageDraw, ImageFilter
import requests
from io import BytesIO
import discord
from discord.ext import commands
from discord.ext.commands import bot
import os

class Images(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def blur(self, ctx, user: discord.User = None):
        if user is None:
            user = ctx.author
        response = requests.get(user.avatar_url)
        img = Image.open(BytesIO(response.content))
        img = img.convert('RGB')
        blurred_image = img.filter(ImageFilter.BLUR)
        blurred_image.save('img.jpg')
        await ctx.send(file=discord.File('img.jpg'))
        os.remove('img.jpg')





def setup(client):
    client.add_cog(Images(client))
