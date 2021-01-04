# Create a discord bot and add it to your server
Follow instructions according to https://discordpy.readthedocs.io/en/latest/discord.html

# Setup after creating Discord bot
Run "source bot-env/bin/activate" in terminal to activate virtual environment \
Run "python3 -m pip install -U requests" and "python3 -m pip install -U discord.py[voice]" in terminal to install dependent libraries \
Install ffmpeg executable from https://ffmpeg.org/ \
Install opus libraries from https://opus-codec.org/downloads/

# Running the bot while in virtual environment
Run "python3 bot.py"

# Supported commands and features
While connected to a Discord voice channel, type "'s <text>" to have the bot speak. Example: "'s hello world" will have the bot say "hello world."\
Type "'language" in a text channel to see all supported languages and "'language <language>" to change to a specific language. Example: "'language Chinese" will change the bot's spoken language to Chinese. 
