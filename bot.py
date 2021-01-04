import os
import discord
from dotenv import load_dotenv
from tts_utils import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
VOICE_CLIENT = None

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	global VOICE_CLIENT
	global DEFAULT_LANG
	global LANGUAGES

	if message.author == client.user:
		return

	if message.content.lower().startswith('\'s'):
		if message.author.voice:
			if message.content == ('\'s'):
				await message.channel.send('No text recognized.')
			else:
				if len(client.voice_clients) == 0:
					VOICE_CLIENT = await message.author.voice.channel.connect()
				else:
					diff_ch = True
					for voice_client in client.voice_clients:
						if voice_client.channel == message.author.voice.channel:
							diff_ch = False
							break
					if diff_ch == True:
						await VOICE_CLIENT.disconnect()
						VOICE_CLIENT = await message.author.voice.channel.connect()
				text = message.content[len('\'s'):]
				text_to_speech(DEFAULT_LANG, text)
				VOICE_CLIENT.play(discord.FFmpegPCMAudio(executable = os.path.abspath(os.getcwd()) + '/ffmpeg', source = os.path.abspath(os.getcwd()) + '/tts.mp3'))
		else:
			await message.channel.send('You must be connected to a voice channel to use this command.')

	if message.content.lower().startswith('\'language'):
		if message.content == ('\'language'):
			avail_lang = "Supported languages: "
			for key in LANGUAGES:
				avail_lang = avail_lang + key + ", "
			await message.channel.send(avail_lang[:len(avail_lang)-2])
		else:
			language = message.content[len('\'language')+1:][0].upper() + message.content[len('\'language')+1:][1:].lower()
			if language in LANGUAGES:
				DEFAULT_LANG = language
				await message.channel.send('Default language changed to ' + language + '.')
			else:
				await message.channel.send(language + ' is not supported.')

client.run(TOKEN)