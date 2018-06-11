import discord
import random
import time
import asyncho
from discord.ext import commands
import os


bot = commands.Bot(command_prefix='!', description="I want to break pacman")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def spam(ctx):
    for i in range(10):
        await ctx.send("SPAMMY SPAM SPAM!")


@bot.command()
async def cookie(ctx, a: str):
    await ctx.send(":cookie: %s" % a)

@bot.command()
async def spamword(ctx, a: str):
    for i in range(1, 10):
        await ctx.send(a)
        time.sleep(1)

@bot.command()
async def lol(ctx):
    meme_list = ["https://b.thumbs.redditmedia.com/svfUDs1-XotHl5kCIpav4F6SC7LkTNataVW9oAC7cWQ.jpg", "https://a.thumbs.redditmedia.com/TuGnQ7V7GrEmaPwUT3GeuDIft93ko8wEIww8qCUusW8.jpg",
     "https://b.thumbs.redditmedia.com/YdvGXlmjecLISmoCdtzmscxH40zAgPceOSv_un7OP5o.jpg", "https://b.thumbs.redditmedia.com/peRkaCT6CmR9QPkBRrZDUXgY8VWR2s4v0FTtRDP8IxA.jpg",
     "https://a.thumbs.redditmedia.com/I6tX7gx9WH7w8zmj85LAnJnmceiBs9rRRVggitpvib0.jpg"]
    await ctx.send(meme_list[random.randint(0, 4)] + (" :laughing:" * random.randint(1, 5)))






bot.run(os.getenv['BOT_TOKEN'])
