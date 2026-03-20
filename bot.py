import os
import random
import discord
from discord.ext import commands

# ---- Intents ----
intents = discord.Intents.default()
intents.message_content = True  # REQUIRED for reading messages

# ---- Bot Setup ----
bot = commands.Bot(command_prefix="!", intents=intents)

# ---- Events ----
@bot.event
async def on_ready():
    print(f"Tester bot online as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # If the bot is tagged in the message
    if bot.user in message.mentions:
        await message.channel.send("You tagged me! I'm alive on Railway.")

    # Allow commands to run
    await bot.process_commands(message)

# ---- Basic Commands ----

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def echo(ctx, *, message: str):
    await ctx.send(message)

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(f"{a + b}")

@bot.command()
async def info(ctx):
    await ctx.send(f"I'm online and running on Railway as {bot.user}!")

# ---- Fun Commands ----

# Magic 8-ball
@bot.command()
async def eightball(ctx, *, question: str):
    responses = [
        "Yes.", "No.", "Absolutely.", "Definitely not.",
        "Ask again later.", "It’s unclear.", "Without a doubt.",
        "My sources say no.", "Probably.", "I don’t think so."
    ]
    await ctx.send(f"🎱 {random.choice(responses)}")

# Coin flip
@bot.command()
async def coinflip(ctx):
    await ctx.send(f"🪙 {random.choice(['Heads', 'Tails'])}")

# Roll a dice
@bot.command()
async def roll(ctx, sides: int = 6):
    if sides < 2:
        await ctx.send("Dice must have at least 2 sides.")
        return
    result = random.randint(1, sides)
    await ctx.send(f"🎲 You rolled a **{result}** on a {sides}-sided die.")

# Choose between options
@bot.command()
async def choose(ctx, *options):
    if len(options) < 2:
        await ctx.send("Give me at least two choices!")
        return
    await ctx.send(f"I choose: **{random.choice(options)}**")

# Rate something
@bot.command()
async def rate(ctx, *, thing: str):
    score = random.randint(1, 10)
    await ctx.send(f"I rate **{thing}** a **{score}/10**")

# ---- Run Bot ----
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
