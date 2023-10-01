import discord
import logging

from discord.ext import commands
from config import TOKEN
from random import randint

logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="latest.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)

def prefix(bot, msg):
    pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.slash_command()
async def rmod(ctx, count: discord.Option(int), d: discord.Option(int)):
    rolls = [randint(1, d) for x in range(count)]
    await ctx.respond(f"D{d} Rolls: {tuple(rolls)}\nModal Total: {max([rolls.count(x)*x for x in range(1, count+1)])}")

@bot.slash_command()
async def proll(ctx, traits: discord.Option(int)):
    rolls = [randint(1, 6) for x in range(traits)]
    async def extra():
        num = randint(1, 6)
        if num == 6:
            await extra()
        rolls.append(num)
    for x in range(rolls.count(6)):
        await extra()
    await ctx.respond(f"Rolls: {tuple(rolls)}\nScore: {list(map(lambda x: x%2==0,rolls)).count(True)}")

@bot.slash_command()
async def summon(ctx):
    await ctx.respond("\'You are a terrible person.\'")

bot.run(TOKEN)