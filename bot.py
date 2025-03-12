import discord
import dotenv
import os
from discord.ext import commands
from groq import Groq

intents = discord.Intents.default()
intents.message_content = True

listaMensajes = []

bot = commands.Bot(command_prefix='?', intents=intents)

dotenv.load_dotenv("project/token.env")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_message(message):
    if list(message.content)[0] != "?":
        if len(listaMensajes) == 10:
            listaMensajes.pop(0)
            listaMensajes.append(message.content)
        else:
            listaMensajes.append(message.content)
        print(message.content)
    else:
        pass
   

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')
    await bot.change_presence(activity=discord.Game(name="Working on..."))

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

@bot.command()
async def resume(ctx):
    serie = ""

    for mensaje in listaMensajes:
        serie += mensaje + ', '

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Resumeme los siguientes mensajes: "
            },
            {
                "role": "user",
                "content": serie,
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    texto_parafraseado = chat_completion.choices[0].message.content
    await ctx.reply(f"📝 **Mensajes resumidos:** {texto_parafraseado}")

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