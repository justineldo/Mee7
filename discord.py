#importing modules
from discord.ext import commands
import discord
import levels

cogs = [levels]

client = commands.Bot[command_prefix='.', intents = discord.Intents.all()] #initiating a client

for i in range(len(cogs)):
    cogs[i].setup(client)
    print('Setup successful.')
    
client.run('token here')
