import discord
import logging

from config import TOKEN
from random import randint

logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="latest.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.slash_command()
async def roll(ctx, count: discord.Option(int), d: discord.Option(int)):
    rolls = [randint(0, d) for x in range(count)]
    await ctx.respond(f"D{d} Rolls: {tuple(rolls)}\nModal Total: {max([rolls.count(x)*x for x in range(1, count+1)])}")

@bot.slash_command()
async def summon(ctx):
    await ctx.respond("\'You are a terrible person.\'")

bot.run(TOKEN)