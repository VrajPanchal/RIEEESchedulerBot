
import discord
import os

my_secret = os.environ['token']
client = discord.Client()
@client.event
async def on_ready():
	print('{0.user}'.format(client) +' is online!')
@client.event
async def on_message(message):
	if message.author == client.user:
		return
	elif message.content.startswith('!setMessage'):
		await message.channel.send('Im alive!')
client.run(my_secret)