import discord
import os

GUILD = os.getenv('DISCORD_GUILD')


class MyClient(discord.Client):
    async def on_ready(self):
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
                                                             name="for messages that start with a dash (-)"))
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == client.user:
            return
        print('Message from {0.author}: {0.content}'.format(message))

        if message.content.startswith('?apple'):
            msg = 'panana'.format(message)
            await message.channel.send(msg)

        if message.content.startswith('?blast'):
            msg = '{0.author.mention} WANTS TO PING'.format(message)
            await message.channel.send(msg)
        if message.content.startswith('?no'):
            msg = 'yes'.format(message)
            await message.channel.send(msg)
        if message.content.startswith('?hi'):
            msg = 'adios'.format(message)
            await message.channel.send(msg)

client = MyClient()
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')





client.run('Nzc1MzU5MTIzNzkzMzc5MzMw.X6lLdA.YrFWMgVXL2ymn73yXMEaUoHOF04')
