import discord
import logging
from discord.ext import commands
import aiohttp
import asyncio
from aiohttp import web


prefix = "!"
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
client = discord.Client()


intents = discord.Intents.default()
intents.typing = False
intents.presences = False

global author_counter
author_counter = 0



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event


async def on_message(message):
    global guild
    guild = message.guild

    global author_counter
    word_list = ['cheat', 'cheats', 'hack', 'hacks', 'internal', 'external', 'ddos', 'denial of service',"shit"]
    if message.author == client.user:
        return
    messageContent = message.content

    if len(messageContent) > 0:
        for word in word_list:


            if word in messageContent:
                author_counter = author_counter + 1
                if author_counter % 3 == 1:
                    await message.delete()
                    await  message.channel.send("Do not say that again{0.author.mention}".format(message))

                elif author_counter % 3 == 2:
                    await message.delete()
                    await message.channel.send(" Shut up now! {0.author.mention}".format(message))
                else:
                    await message.delete()
                    await message.channel.send("Hey! Language {0.author.mention}".format(message))

    messageattachments = message.attachments
    if len(messageattachments) > 0:
        for attachment in messageattachments:
            if attachment.filename.endswith(".dll"):
                await message.delete()
                await message.channel.send("No DLL's allowed!")
            elif attachment.filename.endswith('.exe'):
                await message.delete()
                await message.channel.send("No EXE's allowed!")
            else:
                break

    if message.content.startswith(f'{prefix}hello'):
        await message.channel.send(f'Hello! {message.author}')
    if message.content.startswith(f'{prefix}server'):
        await message.channel.send(f'Got it! {message.guild}')
    if message.content.startswith(f'{prefix}botInfo'):
        await message.channel.send(f'My resume: \n discord version: {discord.__version__}')

    if message.content.startswith(f'{prefix}history'):
        await message.channel.send(f'Your messages history is: \n {messages}')
    if "minecraft" in message.content:
        await message.channel.send("Lets speedrun!")
    if message.content.startswith(f"{prefix}counter"):
        await message.channel.send(f"{author_counter}")
    if message.content.endswith("?"):
        url = f"google.com/search?q={message.content}"
        await message.channel.send(f"copy this link dude, {url}")
    if message.content.endswith("!"):
        await message.add_reaction( '\N{THUMBS UP SIGN}')
    if "create channel" in message.content:

        await guild.create_text_channel('little channel')
    if "delc" in message.content:
        cid = discord.utils.get(guild.text_channels, name="little channel")
        await channel_delete(cid)



client.run('Nzc1MzU5MTIzNzkzMzc5MzMw.X6lLdA.YrFWMgVXL2ymn73yXMEaUoHOF04')
