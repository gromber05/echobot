import discord
import dotenv
import os
from discord.ext import commands
from groq import Groq

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)

dotenv.load_dotenv("project/token.env")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')
    await bot.change_presence(activity=discord.Game(name="Working on..."))

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def parafrasea(ctx, *args):

  texto_original = " ".join(args)  

  chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Parafrasea el siguiente texto: "
            },
            {
                "role": "user",
                "content": texto_original,
            }
        ],
        model="llama-3.3-70b-versatile",
    )

  texto_parafraseado = chat_completion.choices[0].message.content
  await ctx.reply(f"📝 **Texto parafraseado:** {texto_parafraseado}")

@bot.command()
async def traduce(ctx, *args):

  texto_original = " ".join(args)  

  chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Traduceme el siguiente texto al español: "
            },
            {
                "role": "user",
                "content": texto_original,
            }
        ],
        model="llama-3.3-70b-versatile",
    )

  texto_traducido = chat_completion.choices[0].message.content
  await ctx.reply(f"📝 **Texto traducido:** {texto_traducido}")

# Parte de tokens

bot.run(TOKEN)