import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = os.getenv("COMMAND_PREFIX", "!")

# Intents
intents = discord.Intents.default()
intents.message_content = True

# Initialize the bot
bot = commands.Bot(command_prefix=PREFIX, intents=intents)


@bot.event
async def on_ready():
    # Prints the hello message for server side shit
    print(f"{bot.user.name} has connected to Discord!")
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

    # Load all cogs in the cogs/ folder
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py") and not filename.startswith("_"):
            cog_name = f"cogs.{filename[:-3]}"
            try:
                await bot.load_extension(cog_name)
                print(f"Loaded {cog_name}")
            except Exception as e:
                print(f"Failed to load cog {cog_name}: {e}")

    await bot.tree.sync()


@bot.event
async def on_


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found. Type `!help` for a list of commands.")
    else:
        raise error


if __name__ == "__main__":
    bot.run(TOKEN)
