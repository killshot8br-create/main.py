import os
import discord
from discord.ext import commands

# --------------------------------------------------
# [1] حط التوكن حقك بين الأقواس (بداخل علامات التنصيص)
# --------------------------------------------------
TOKEN = "MTQ2MDQxMDI3MzI0NzY2MjM0NQ.Gsjkkn.58Pow-H-LGTCNqXigdrRioqOn0WrtsMzz6TV2I"

# [2] حط آي دي (ID) الروم الصوتي هنا (أرقام فقط)
CHANNEL_ID = 1266590063521697872

bot = commands.Bot(command_prefix="!", self_bot=True)

@bot.event
async def on_ready():
    print(f"------------------------------------------")
    print(f"تم تسجيل الدخول بنجاح كـ: {bot.user}")
    print(f"------------------------------------------")
    
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        try:
            await channel.connect(reconnect=True, self_deaf=True)
            print(f"[✔] تم الانضمام للروم الصوتي: ({channel.name}) بنجاح!")
        except Exception as e:
            print(f"[✖] فشل الانضمام للروم: {e}")
    else:
        print("[✖] لم يتم العثور على الروم الصوتي! تأكد من صحة CHANNEL_ID وأن الحساب يشوف الروم.")

bot.run(TOKEN)
