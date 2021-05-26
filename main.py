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

import requests
from discord import RawReactionActionEvent
from channel_ignore import chan_ignore
# IMPORT COMMANDS FROM THE DISCORD.EXT MODULE.
from discord.ext import commands, tasks
# Import load_dotenv function from dotenv module.
from dotenv import load_dotenv
# from discord.utils import get
from discord import utils
from datetime import datetime
from time import time

# SECTION: Startup and bot loading section
# Here's code contains commands when bot startup
# And It comes to load with this shit
# YES


# Loads the .env file that resides on the same level as the script.
load_dotenv()

# Grab the API token from the .env file.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Bot's privilege performance
intents = discord.Intents.all()
# CREATES A NEW BOT OBJECT WITH A SPECIFIED PREFIX. IT CAN BE WHATEVER YOU WANT IT TO BE.
bot = commands.Bot(command_prefix="?", intents=intents)
# discord.AuditLogDiff(roles)

# Connect to SQLITE3 BASE
conn = sqlite3.connect('orbit.db')


# SECTION 2: What's more guilds?
def __init__(self, bot):
    super().__init__()
    self.bot = bot

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

    # Bot status presence
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,
                                                        name='участников'))

    # PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
    print("Бот на станции " + str(guild_count) + " серверов.")

#    channelhd = bot.get_channel()
#    role = discord.utils.get(user.server.roles, name="CSGO_P")
#    message = await bot.send_message(channel, "React to me!")
#    while True:
#        reaction = await bot.wait_for_reaction(emoji="🏃", message=message)
#        await bot.add_roles(reaction.message.author, role)
#
#    emoj = '\:syringe:'
#    channelst = bot.get_channel(805206795895308319)
#    await channelst.send('Ты можешь нажать на реакцию, чтобы получить дополнительный доступ к категории "DARK"')
#    if message.content == channelst:
#        await message.add_reaction(emoj)

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


# embed=discord.Embed(title=ДАРК, url=https://res.cloudinary.com/redys/image/upload/v1617568573/1d344b00edd680dda90b03e6727844b2_gl2m0a.png, description=Если вы любитель дарк-контента, то можете получить роль, которая даст вам дополнительные возможности на этом сервере. Нажми - :syringe: если ты дарк, color=0x7c0e0e)
# embed.set_author(name=Получение ролей, icon_url=https://res.cloudinary.com/redys/image/upload/v1617568811/noun_User_role_281793_icaehb.png)
# embed.add_field(name=undefined, value=undefined, inline=False)
# await ctx.send(embed=embed)
# Basic command resolve on ping. Replying by pong
@bot.command(
    # Помощь
    help="Тестовая команда бота для проверки работа команд"
)
async def ping(ctx):
    await ctx.channel.send("pong")


#@bot.command()
#async def displayembed():
#    embed = discord.Embed(
#        title = 'Заголовок',
#        description = 'Описание',
# #       colour = discord.Colour.from_rgb(106, 192, 245)
#    )
#    await bot.say(embed=embed)


# SECTION 3: Member join event


# LISTEN WHEN NEWBIE JOINS TO DISCORD SERVER
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(769653758363566090)
#    memberuser = utils.find(lambda r: r.name == 'Брони', member.guild.roles)
#    if memberuser in member.guild.roles:
#        print('Member already has role')
#    else:
#        await member.add_roles(utils.get(member.guild.roles, id=776880603152908310))
    await member.send("Привет путник, у тебя есть 10 минут на то, чтобы принять **правила нашего сервера.**")
    nowtime = int(time())
    while member.pending:
        if int(time()) - nowtime >= 600:
            print(f'{member} не принял правила, в этом случае он будет кикнут из сервера')
            await member.send("Вас кикнули из сервера потому что вы не приняли правила, вы можете попробовать снова принять правила, перейдя по ссылке: https://discord.gg/MSW6eSm388")
            await member.kick(reason=f'{member} не принял правила за указанное время')
            return
        await asyncio.sleep(1)
    await member.add_roles(utils.get(member.guild.roles, id=769663582849204234))
    await member.send(f'Вы приняли правила {member.mention}! '
                       f'Добро пожаловать к нам на сервер путник <:eldrinko:770199830847946803>')

# Logger life in log-file
logger = logging.getLogger('discord')
logging.basicConfig(level=logging.DEBUG)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename=r'C:\Users\crazy\Desktop\friendbot\logs\discord-{:%Y-%m-%d %H-%M-%S}.log'.format(datetime.now()), encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)



url = "https://discord.com/api/webhooks/830351578338426900/4SAL2aaw-ND-DgOyzuEKzjrn9kDA80jgZ412jWBU6Y2xzT2nDAkCmIz1FqfOfmSeX81l"
timeout = 5
try:
    requests.get(url, timeout=timeout)
    print(f"ВИЖУ ПИТАНИЕ! МОЛОДЕЦ САНЯ!")
except (requests.ConnectionError, requests.Timeout ) as exception:
    print("Я потерял соединение, быстро дайте мне педаль в руки!.")

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run(DISCORD_TOKEN)
