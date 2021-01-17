# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord

# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
bot = discord.Client()

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
	print(message.content)
	# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
	if message.content == "Привет <@!800147221722300477>":
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		await message.channel.send("Здравствуй, я несу дружбомагию")
	if message.content == "<@!800147221722300477> ты гей?":
		await message.channel.send("Я носитель дружбомагии")
	if message.content == "<@!800147221722300477> кто такой Хабар?":
	    await message.channel.send("Вождь нескольких групп и этого сервера Дискорд")


# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run("ODAwMTQ3MjIxNzIyMzAwNDc3.YAN5Kw.iZ7uMwBDH4BTgO7H0nPY7FjuG6U")