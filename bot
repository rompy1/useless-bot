import discord
import random
import time
from discord.ext import commands


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
    meme = https://www.reddit.com/r/ComedyCemetery/comments.json?limit=1["link_url"]
    await ctx.send(meme + (" :laughing:" * random.randint(1, 5)))





bot.run(os.environ['BOT_TOKEN'])
