import discord
from discord.ext import commands
import random

TOKEN = "Bot Token :)"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

tips = [
    "Gunakan botol minum isi ulang daripada membeli air kemasan.",
    "Bawa tas belanja sendiri saat berbelanja.",
    "Pisahkan sampah organik dan anorganik di rumah.",
    "Manfaatkan kembali botol atau kardus bekas.",
    "Kurangi penggunaan sedotan sekali pakai.",
    "Gunakan wadah makan yang bisa dipakai berulang kali.",
    "Bawa alat makan sendiri saat membeli makanan.",
    "Gunakan sapu tangan daripada tisu sekali pakai.",
    "Perbaiki barang yang rusak jika masih bisa digunakan.",
    "Donasikan pakaian yang sudah tidak dipakai tetapi masih layak.",
    "Gunakan dokumen digital untuk mengurangi penggunaan kertas.",
    "Komposkan sisa sayur dan buah jika memungkinkan.",
    "Gunakan gelas daripada cangkir sekali pakai.",
    "Pisahkan sampah elektronik dari sampah biasa.",
    "Gunakan kembali kantong plastik yang masih layak pakai.",
    "Beli hanya barang yang benar-benar dibutuhkan.",
    "Pilih produk dengan kemasan yang dapat didaur ulang.",
    "Gunakan tumbler saat pergi ke sekolah atau bepergian.",
    "Jual atau berikan barang yang sudah tidak digunakan daripada membuangnya.",
    "Ajak keluarga untuk mulai memilah sampah bersama."
]

@bot.event
async def on_ready():
    print(f"Bot aktif sebagai {bot.user}")

@bot.command()
async def tip(ctx):
    await ctx.send(
        f" **Tips Ramah Lingkungan**\n\n{random.choice(tips)}"
    )

@bot.command()
async def helpeco(ctx):
    await ctx.send(
"""
 **Eco Tips Bot**

Perintah yang tersedia:
`/tip` - Menampilkan tips ramah lingkungan secara acak.
`/helpeco` - Menampilkan daftar perintah bot.
"""
    )

bot.run(TOKEN)
