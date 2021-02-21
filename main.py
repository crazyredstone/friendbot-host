# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord
# Import OS module. 
import os
# Import Logging System.
import logging
# Import what
import asyncio
# HTTP
import aiohttp
# Status
import status
# IMPORT COMMANDS FROM THE DISCORD.EXT MODULE.
from discord.ext import commands
from pip._internal.network import session
from discord import channel
# Import load_dotenv function from dotenv module.
from dotenv import load_dotenv
from asyncio.tasks import async
# Importing SQLITE3
import sqlite3

# Logger life in log-file
		logger = logging.getLogger('discord')
		logger.setLevel(logging.DEBUG)
		handler = logging.FileHandler(filename='discord-log.log', encoding='utf-8', mode='w')
		handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
		logger.addHandler(handler)
		logging.basicConfig(level=logging.INFO)

# Loads the .env file that resides on the same level as the script.
load_dotenv()

# Grab the API token from the .env file.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
bot = discord.Client()
# CREATES A NEW BOT OBJECT WITH A SPECIFIED PREFIX. IT CAN BE WHATEVER YOU WANT IT TO BE.
bot = commands.Bot(command_prefix="!")

# discord.AuditLogDiff(roles)

# Connect to SQLITE3 BASE
conn = sqlite3.connect('redies.db')

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
	guild_count = 0

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
	for guild in bot.guilds:
		# PRINT THE SERVER'S ID AND NAME.
		print(f"- {guild.id} (название: {guild.name})")

		# INCREMENTS THE GUILD COUNTER.
		guild_count = guild_count + 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
	print("Бот на станции " + str(guild_count) + " серверов.")

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
	print('{0.author}: {0.content}'.format(message))
	# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
	if message.content == "<@!800147221722300477> привет":
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		channel = message.get_channel(769652253047914520)
		await message.channel.send("Здравствуй, я несу дружбомагию")
	if message.content == "<@!800147221722300477> ты гей?":
		await message.channel.send("Я носитель дружбомагии")
	if message.content == "<@!800147221722300477> кто такой Хабар?":
		await message.channel.send("Вождь нескольких групп и этого сервера Дискорд")
	if message.content == ("арсен говнов)")
		await message.channel.send("арсен говнов)")
	# INCLUDES THE COMMANDS FOR THE BOT. WITHOUT THIS LINE, YOU CANNOT TRIGGER YOUR COMMANDS.
	await bot.process_commands(message)

# Basic command resolve on ping. Replying by pong
@bot.command(
	# Помощь
	help="Тестовая команда бота"
)
async def ping(ctx):
	await ctx.channel.send("pong")

# Функционал отменён.
# Убирает и возвращает роль

async def main():
	await asyncio.sleep(10)
	async with aiohttp.ClientSession() as session:
		async with session.get('http://aws.random.cat/meow') as r:
			if r.status == 200:
				js = await r.json()
				await channel.send(js['file'])

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run(DISCORD_TOKEN)