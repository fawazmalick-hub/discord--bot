import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

TARGET_CHANNEL_ID = 1507273946012323961  

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.event
async def on_message(message):
    if message.webhook_id is None and message.author .bot :
           return

    if message.channel.id == TARGET_CHANNEL_ID:
        try:
            user = await bot.fetch_user(590074923284955136) 
            await user.send(
                f"📩 {message.author}: {message.content}"
            )
        except Exception as e:
            print(e)

    await bot.process_commands(message)

bot.run(os.getenv("DISCORD_TOKEN"))
