import discord
import os
import requests
import asyncio
from json import loads
client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("League of Legends")
    await client.change_presence(status=discord.Status.online, activity=game)
    twitch = "puppybin2"
    name = "강하지"
    channel = client.get_channel(805770868319584307)
    a = 0
    while True:
        headers = {'Client-ID': '37jxkyyjsdz48r3gnz9qwcy52hj2sz'}
        response = requests.get("https://api.twitch.tv/helix/streams?user_login=" + twitch, headers=headers)
        try:
            if loads(response.text)['data'][0]['type'] == 'live' and a == 0:
                await channel.send("@everyone 강하지 방송중! ʕ •ɷ•ʔฅ")
                a = 1
        except:
            a = 0
        await asyncio.sleep(5)

@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("반가워")
        a = 0
    if message.content.startswith("강하지"):
        await message.channel.send("골딱이")
        a = 0
    if message.content.startswith("개새끼"):
        await message.channel.send("멍멍")
        a = 0


access_token = os.environ['BOT_TOKEN']
client.run(access_token)
