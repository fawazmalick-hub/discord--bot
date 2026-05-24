import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

🔴 PUT YOUR CHANNEL ID HERE
TARGET_CHANNEL_ID = 1507273946012323961  # replace this

When bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

Listen to all messages
@bot.event
async def on_message(message):
    # ignore bot itself
    if message.author.bot:
        return

    # only listen to one channel
    if message.channel.id == TARGET_CHANNEL_ID:
        try:
            # send to your DMs
            user = await bot.fetch_user(590074923284955136)  # replace this
            await user.send(
                f"📩 {message.author}: {message.content}"
            )
        except Exception as e:
            print(e)

    await bot.process_commands(message)

bot.run(os.getenv("DISCORD_TOKEN"))
