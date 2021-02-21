import discord
from discord.client import Client

async def client(change_presence):
	activity = discord.Activity(name='тебя', type=discord.ActivityType.listening)
	await change_presence(activity=activity)

