import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import yt_dlp
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot conectado como {bot.user.name}')
    await bot.change_presence(activity=discord.Game(name="🎵 ¡Listo para la música!"))

# 🔊 Conectarse al canal de voz
@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(f'🔊 Conectado al canal: {channel}')
    else:
        await ctx.send("⚠️ ¡Debes estar en un canal de voz!")

# ⏹️ Salir del canal de voz
@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("👋 Desconectado del canal de voz")
    else:
        await ctx.send("❌ No estoy en ningún canal de voz")

# ▶️ Reproducir música
@bot.command()
async def play(ctx, url):
    voice_client = ctx.voice_client
    if not voice_client:
        await ctx.send("❗ Usa `!join` para conectarme a un canal de voz.")
        return

    YDL_OPTIONS = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'quiet': True,
        'default_search': 'ytsearch'
    }

    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn'
    }

    try:
        with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            audio_url = info['url']
            title = info.get('title', 'Desconocido')

        await ctx.send(f'🎶 Reproduciendo: **{title}**')

        voice_client.stop()  # Detiene cualquier audio previo
        source = FFmpegPCMAudio(audio_url, **FFMPEG_OPTIONS)
        voice_client.play(source)

    except Exception as e:
        await ctx.send(f'⚠️ Error al reproducir: {str(e)}')

# ⏹️ Detener reproducción
@bot.command()
async def stop(ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
        ctx.voice_client.stop()
        await ctx.send("⏹️ Reproducción detenida.")
    else:
        await ctx.send("❌ No hay música reproduciéndose.")

# Parte de IA

OPENAI_API_TOKEN = '~'

TOKEN = '~'
bot.run(TOKEN)