import discord

class MyClient(discord.Client):
	async def on_ready(self):
			print('Logged on as {0}!'.format(self.user))

	async def on_message(self, message):
     		

client = MyClient()