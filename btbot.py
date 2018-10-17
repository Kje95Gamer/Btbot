import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.Client ()
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()

chat_filter = ["FUCK", "SHIT", "WTF", "WTH", "MOTHERFUCKER", "A7A", "NUB", "NOOB"]

@client.event
async def on_ready():
    print("The Bot is Ready")


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Welcome! To The Brothers Town')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='Moin Cwaft'))
    print('Ready') 


@client.event
async def on_message(message):
    
    if message.content.upper().startswith('BOT'):
        randomlist = ["I AM A BOT, DAAAB","Ay, How are you ?"]
        await client.send_message(message.channel,(random.choice(randomlist)))
        
    if message.content.upper().startswith('BT/8BALL'):
        randomlist = ["Nope","Yep","Maybe"]
        await client.send_message(message.channel,(random.choice(randomlist)))
        
    if message.content.upper().startswith('PING'):
        await client.send_message(message.channel,'Pong!')
        
    if message.content.upper().startswith('BT/RULES'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> **Rule1** Never swear or be a nerd, **Rule2** Don't spam in any chat, **Rule3** Don't move the music bot from the music category!" % (userID))

    if message.content.upper().startswith("BT/SAY"):
        if "497816085203124232" in [role.id for role in message.author.roles]:
            args = message.content.split(" ")
            await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        else:
            await client.send_message(message.channel, "You are not a staff!")
        
    #Chat Filter 
    contents = message.content.split(" ")
    for word in contents:
        if word.upper() in chat_filter:
            try:
                await client.delete_message(message)
                userID = message.author.id
                await client.send_message(message.channel, "<@%s> **Hey!** Dont Swear :anger:" % (userID))
            except discord.errors.NotFound:
                return
    
    
client.run('NTAwMDYyMjQ4MzU0NzA5NTM1.DqFXBg.vXDNZfqCFj9m6w2but9mKyQJb-E')
