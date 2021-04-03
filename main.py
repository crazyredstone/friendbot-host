# Import
import asyncio
# Import Logging System.
import logging
# Import OS module.
import os
import sqlite3
# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord
import datetime
# from discord import user
from channel_ignore import chan_ignore
# IMPORT COMMANDS FROM THE DISCORD.EXT MODULE.
from discord.ext import commands, tasks
# Import load_dotenv function from dotenv module.
from dotenv import load_dotenv
# from discord.utils import get
from discord import client, utils
from discord import channel
from datetime import datetime
from discord import member

# Loads the .env file that resides on the same level as the script.
load_dotenv()

# Grab the API token from the .env file.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
# bot1 = discord.Client()
# CREATES A NEW BOT OBJECT WITH A SPECIFIED PREFIX. IT CAN BE WHATEVER YOU WANT IT TO BE.
bot = commands.Bot(command_prefix="?")

# discord.AuditLogDiff(roles)

# Connect to SQLITE3 BASE
conn = sqlite3.connect('redies.db')


# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
    # CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
    guild_count: int = 0

    # LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
    for guild in bot.guilds:
        # PRINT THE SERVER'S ID AND NAME.
        print(f"- {guild.id} (название: {guild.name})")

        # INCREMENTS THE GUILD COUNTER.
        guild_count = guild_count + 1

    # Must work with status bot
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,
                                                        name='участников'))

    # PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
    print("Бот на станции " + str(guild_count) + " серверов.")


# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
    now_message = datetime.now()
    dt_string_message = now_message.strftime("%d/%m/%Y %H:%M:%S")
    if message.author.id == 800147221722300477:
        return
    if message.channel.id in chan_ignore:
        return
    print(
        f'{dt_string_message}' + (
            ' Message from: channel: {0.channel} --> user: {0.author}: message: {0.content}'.format(message)))
    # CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
    if message.content == "<@!800147221722300477> привет":
        # SENDS BACK A MESSAGE TO THE CHANNEL.
        await message.channel.send("Здравствуй, я несу дружбомагию")
    if message.content == "<@!800147221722300477> ты кто?":
        await message.channel.send("Я носитель дружбомагии")
    if message.content == "<@!800147221722300477> зачем пришёл сюда?":
        await message.channel.send("Чтобы нести дружбомагию в ваш прекрасный сервер." + "<:scootalook:809402090253451316>")
    if message.content == "<@!800147221722300477> кто такой Хабар?":
        await message.channel.send("Вождь MaM и этого сервера Дискорд")
    if message.content == "арсен говнов)":
        await message.channel.send("арсен говнов)")

    # INCLUDES THE COMMANDS FOR THE BOT. WITHOUT THIS LINE, YOU CANNOT TRIGGER YOUR COMMANDS.
    await bot.process_commands(message)


async def on_member_join(member):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(f'{dt_string}: Новый участник {member} зашёл на сервер', 'Прежде чем войти ему требуется принять правила сервера',
            sep='\n')
    await asyncio.sleep(2)

    channel = await member.create_dm()
    await channel.send("Привет, у тебя есть 10 минут, на то, чтобы принять правила")
    if member.pending():
        member.addroles(utils.get(member.guild.roles, id="769663582849204234"))
    else:
        await asyncio.sleep(600)
        print(f'{dt_string}')
        print(f'{member} не принял правила, в этом случае он будет кикнут')
        member.kick(reason=f'{member} не принял правила')

# Basic command resolve on ping. Replying by pong
# TODO: Fix command bot
@bot.command(
    # Помощь
    help="Тестовая команда бота"
)
async def ping(ctx):
    await ctx.channel.send("pong")

# Logger life in log-file
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord-{:%Y-%m-%d %H-%M-%S}.log'.format(datetime.now()), encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Gotta take the role and return it's back.(but that does not work, because function has cancelled)

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run(DISCORD_TOKEN)
