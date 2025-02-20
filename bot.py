import discord
import dotenv
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

os.system("cls" if os.name == "nt" else "clear")

bot = commands.Bot(command_prefix='?', intents=intents)

listaMensajes = list()

@bot.event
async def on_ready():
    print(f'✅ Bot conectado como {bot.user.name}')
    await bot.change_presence(activity=discord.Game(name="Working on..."))

@commands.Cog.listener()
async def on_message(self, message:discord.Message):
    listaMensajes.append(message)
    print("\n" + message)


@commands.Cog.listener()
async def on_error(self, event:str, *args, **kwargs):
    await print("Error, comando no encontrado")

# Parte de tokens

dotenv.load_dotenv("project/token.env")

OPENAI_API_TOKEN = os.getenv("OPENAI_TOKEN")

TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)