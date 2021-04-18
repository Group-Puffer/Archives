
import discord 
from discord.ext import commands
from discord.utils import get
import urllib.parse, urllib.request, re
import json 
from pathlib import Path                #All of these were from Puffer (still closed source) and removed some unnecessary ones, but still kept some just to be safe.
import logging
import asyncio
import subprocess
from async_timeout import timeout
import time
#________________________________________________________________________________________

bot = discord.Client()

bot = commands.Bot(command_prefix="b!", case_insensitive=True)

bot.remove_command('help')

embedcolor = color=0x00ff00 #Light green. (Puffer's main embed color)

errorcolor = color=0xe74c3c #Red

async def is_owner(ctx):

    return ctx.author.id == (your user id goes here)


@bot.event
async def on_ready():
    print(f"-----\nLogged in as: {bot.user.name} : {bot.user.id} \nTotal Servers:"+ str(len(bot.guilds)))


@bot.command()
async def autobump(ctx):
    while True:
            await ctx.send("!d bump")
            await asyncio.sleep(5) #This was to test the loop and bump.

bot.loop.create_task(autobump())

@bot.command()
@commands.check(is_owner)
async def logout(ctx, *, reason=None):
    await ctx.send(f"Logging Out. \n `Reason: {reason}`")




bot.run("Bot token") #Please don't put a user token, even though you can't achieve bumps without a normal user.
