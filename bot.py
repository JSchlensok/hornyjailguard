import os

import discord
from discord.ext.commands import Bot, errors
from discord import Member, User, VoiceChannel
from dotenv import load_dotenv

from PIL import Image, ImageFont, ImageDraw

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_NAME = os.getenv('CHANNEL_NAME')

bot = Bot('-')

@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord")

@bot.command(name='bonk')
async def putIntoHornyJail(ctx, member: Member):

    # Generate meme
    img = Image.open("horny_jail_blank.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 75)
    draw.text((50, 10), f"Go to horny jail, {member.display_name}!", (0,0,0), font=font)
    img.save('generated_meme.jpg')

    # Post meme
    file = discord.File("generated_meme.jpg")
    await ctx.send(f"Go to horny jail, {member.mention}!", file=file)


    # Move to horny jail voice channel
    channel = discord.utils.get(ctx.guild.channels, name=CHANNEL_NAME)
    await member.move_to(channel)

bot.run(TOKEN)
