import discord
import random
from discord.ext import commands
import os
import asyncio
import youtube_dl


client = commands.Bot(command_prefix= '!', intents=discord.Intents.all())
voiceclients = {}
yt_dl_options = {'format' : 'bestaudio/best'}
ytdl = youtube_dl.YoutubeDL(yt_dl_options)
ffmpeg_opts = {'options' : "-vn"} 
@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def insult(ctx):
    file = open("botwords.txt", "r", encoding = "utf-8")
    mylist = []
    for line in file:
        mylist.append(line)
    await ctx.send(random.choice(mylist)) 
    print("Message sent")
        
@client.event
async def on_message(ctx):
    if(ctx.content.startswith("!play")):
        try:
            url = ctx.content.split()[1]
            voice_client = await ctx.author.voice.channel.connect()
            voiceclients[voice_client.guild.id] = voice_client
            loop = asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download = False))
            song = data['url']
            player = discord.FFmpegAudio(song, **ffmpeg_opts)
            voice_client.play(player)
        except Exception as err:
            print(err)
client.run("MTE5NTQwMDMwMzQ5NTg4NDg2MA.GECUS5.m7ZiqUKuW5cWoo2KuXxxDjH5X-wQZ_cfdI54yw")

