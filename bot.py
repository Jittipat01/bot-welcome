import discord
from discord.ext import commands
import os

# ตั้งค่า Intents
intents = discord.Intents.default()
intents.members = True # จำเป็นสำหรับการตรวจจับสมาชิก

bot = commands.Bot(command_prefix="!", intents=intents)

# กำหนด ID ของช่องที่ต้องการให้แจ้งเตือน
# วิธีหา ID: เปิด Developer Mode ใน Discord > คลิกขวาที่ชื่อห้อง > Copy ID
CHANNEL_ID = 1477572378971082933 # <<< เปลี่ยนเป็น ID ห้องของคุณ

@bot.event
async def on_ready():
    print(f'บอทออนไลน์แล้ว: {bot.user.name}')

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(f'🎉 ยินดีต้อนรับคุณ {member.mention} เข้าสู่เซิร์ฟเวอร์!')

# รันบอทโดยใช้ Token จาก Developer Portal
bot.run(os.environ['DISCORD_TOKEN'])