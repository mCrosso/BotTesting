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
    async def whois(self, ctx, user: discord.User = None):
        if user is None:
            user = ctx.author
        response = requests.get(user.avatar_url)
        img = Image.open(BytesIO(response.content))
        #----------------------------------------------------------------------
        img_fraction = 0.50
        W, H = (128, 128)
        fs = 1
        txt = f'This is {user.name}.'
        font_type = ImageFont.truetype('arial.ttf', 30)
        while font_type.getsize(txt)[0] < img_fraction * img.size[0]:
            fs += 1
            font_type = ImageFont.truetype("arial.ttf", fs)
        # ----------------------------------------------------------------
        draw = ImageDraw.Draw(img)
        w, h = draw.textsize(txt)
        draw.text(((W - w) / 2, (H - h) / 2), text=txt, fill=(255, 255, 255), font=font_type)
        img = img.convert('RGB')
        img.save('img.jpg')
        await ctx.send(file=discord.File('img.jpg'))

    @commands.command(pass_context=True)
    async def blur(self, ctx, user: discord.User = None):
        if user is None:
            user = ctx.author
        response = requests.get(user.avatar_url)
        img = Image.open(BytesIO(response.content))
        blurred_image = img.filter(ImageFilter.BLUR)
        blurred_image = blurred_image.convert('RGB')
        blurred_image.save('img.jpg')
        await ctx.send(file=discord.File('img.jpg'))
        os.remove('img.jpg')

def setup(client):
    client.add_cog(Images(client))
