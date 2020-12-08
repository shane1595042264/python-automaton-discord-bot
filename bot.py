import discord
import logging
from discord.ext import commands
import aiohttp
import asyncio
from aiohttp import web
from discord.ext import commands
from discord.ext.commands import Bot
import random

prefix = "!"
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)

client = discord.Client()

intents = discord.Intents().all()  # this is a new thing
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
# It's a initiator for people to get role
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    moji = await bot.get_channel(775355712271941647).send("react/uncheck 🏃 to get/remove banana role "
                                                          "\nreact 🍌 to get banana ")
    await moji.add_reaction(emoji='🏃')
    await moji.add_reaction(emoji="🍌")  # a banana invoker


counter = 0


# impementation for adding reaction to get role
@bot.event
async def on_reaction_add(reaction, user):
    global counter
    channel = bot.get_channel(775355712271941647)

    if reaction.emoji == "🏃":
        role = discord.utils.get(user.guild.roles, name="banana")
        await user.add_roles(role)

    # now you can get banana picture by adding banana reaction
    elif reaction.emoji == "🍌":
        counter += 1
        if counter == 1:
            pass
        else:
            await channel.send(file=discord.File('banana.jpg'))


# This is for people who want to remove their banana role, they can just simply cancel the reaction
@bot.event
async def on_reaction_remove(reaction, user):
    if reaction.emoji == "🏃":
        role = discord.utils.get(user.guild.roles, name="banana")
        await  user.remove_roles(role)


# member new or old. It could get how long you've been in server.
class JoinDistance:
    def __init__(self, joined, created):
        self.joined = joined
        self.created = created

    @property
    def time(self):
        return self.joined - self.created


class JoinDistanceConverter(commands.MemberConverter):
    async def convert(self, ctx, argument):
        member = await super().convert(ctx, argument)
        return JoinDistance(member.joined_at, member.created_at)


@bot.command()
async def time(ctx, *, member: JoinDistanceConverter):
    is_new = member.time.days < 100
    if is_new:
        await ctx.send(f"Hey you're pretty new! You've only been here for{member.time.days} days")
    else:
        await ctx.send(f"Hm you're not so new. You've been here for {member.time.days} days")


# Poker. You can use this to poke someone.
class Slapper(commands.Converter):
    async def convert(self, ctx, argument):
        to_slap = random.choice(ctx.guild.members)
        return '{0.author} poked {1} because *{2}*'.format(ctx, to_slap, argument)


@bot.command()
async def poke(ctx, *, reason: Slapper):
    await ctx.send(reason)


# order food
@bot.command()
async def food(ctx, *args):
    await ctx.send('WE need to eat {} objects: {}'.format(len(args), ', '.join(args)))


# add numbers
@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)


# make arguements to upper case
def to_upper(argument):
    return argument.upper()


@bot.command()
async def up(ctx, *, content: to_upper):
    await ctx.send(content)


author_counter = 0  # for language detection 


# Some message reactions
@client.event
async def on_message(message):
    global guild, author_counter

    guild = message.guild
    # Language detection system

    word_list = ['cheat', 'cheats', 'hack', 'hacks', 'internal', 'external', 'ddos', 'denial of service', "shit"]
    if message.author == client.user:
        return
    messageContent = message.content

    if len(messageContent) > 0:
        for word in word_list:

            if word in messageContent:
                author_counter = author_counter + 1
                if author_counter % 3 == 1:
                    await message.delete()
                    await message.channel.send("Do not say that again{0.author.mention}".format(message))

                elif author_counter % 3 == 2:
                    await message.delete()
                    await message.channel.send(" Shut up now! {0.author.mention}".format(message))
                else:
                    await message.delete()
                    await message.channel.send("Hey! Language {0.author.mention}".format(message))
    # Detect message attachments
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
    # Hello reaction
    if message.content.startswith(f'{prefix}hello'):
        await message.channel.send(f'Hello! {message.author}')
    # Server name response
    if message.content.startswith(f'{prefix}server'):
        await message.channel.send(f'Got it! {message.guild}')
    # Bot Info
    if message.content.startswith(f'{prefix}botInfo'):
        await message.channel.send(f'My resume: \n discord version: {discord.__version__}')
    # Minecraft Reaction
    if "minecraft" in message.content:
        await message.channel.send("Lets speedrun!")
    # Check language counter
    if message.content.startswith(f"{prefix}counter"):
        await message.channel.send(f"{author_counter}")
    # Send search link
    if message.content.endswith("?"):
        url = f"google.com/search?q={message.content}"
        await message.channel.send(f"copy this link dude, {url}")
    # No special usage, just for fun. It will react thumbs up everytime you type a sentence ended with !
    if message.content.endswith("!"):
        await message.add_reaction('\N{THUMBS UP SIGN}')
    # To create a channel
    if "create channel" in message.content:
        await guild.create_text_channel('little channel')


bot.run('Nzc1MzU5MTIzNzkzMzc5MzMw.X6lLdA.X56myM7FE7b8EwRfU35LKxn-20s')
