import os
from dotenv import load_dotenv

import discord
from discord.ext import commands
import random
import datetime

load_dotenv(override=True)

imtiyazlar = discord.Intents.all()
imtiyazlar.message_content = True

piton = commands.Bot(command_prefix="/", intents=imtiyazlar)

@piton.event
async def on_ready():
    print(f"{piton.user} olarak giriş yapıldı!")

@piton.command()
async def merhaba(ctx):
    await ctx.send("merhaba")

@piton.command()
async def zar(ctx):
    sayi = random.randint(1, 6)
    await ctx.send(f"{sayi} geldi!")

@piton.command()
async def tarih(ctx):
    bugun = datetime.datetime.now().strftime("%d.%m.%Y")
    await ctx.send(f"Bugünün tarihi: {bugun}")

@piton.command()
async def yazitura(ctx):
    sonuc = random.choice(["Yazı", "Tura"])
    await ctx.send(f"Sonuç: {sonuc}")

@piton.command()
async def bilgi(ctx):
    await ctx.send("Kullanabileceğin komutlar: /merhaba, /zar, /tarih, /yazitura, /bilgi, /sil")

@piton.command()
@commands.has_permissions(manage_messages=True)
async def sil(ctx, miktar: int):
    await ctx.channel.purge(limit=miktar + 1)
    await ctx.send(f"{miktar} mesaj silindi!", delete_after=3)

@piton.after_invoke
async def komut_sonrasi_mesaji_sil(ctx):
    try:
        await ctx.message.delete()
    except discord.Forbidden:
        pass

piton.run(os.getenv("DISCORD_TOKEN"))
