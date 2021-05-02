# Too much comments ahead, made for a newbie by a newbie to understand
# Import discord and Regex
import discord
from discord.ext import commands
import re

# Define the bot variable with the command prefix of "cp!".
bot = commands.Bot(command_prefix='cp!')
# Read a file called uwu.txt and put it inside a code block.
textstuff = "```" + open("uwu.txt").read() + "```"


@bot.event
async def on_message(message):
    # If the person who sent the message is our bot then don't do anything
    if message.author.bot:
        return

    # The code below checks for the word "stringtest" in a message using Regex then sends the message "test".
    test_pattern = r"(?:^|\W)stringtest(?:$|\W)"  # Define the regex
    # Search using the Regex test_pattern in the Message after
    # lower-casing it.
    if re.search(test_pattern,
                 message.content.lower()) is not None:

        # Send a message to the channel, the message being "test".
        channel = message.channel
        await channel.send("test")

    # In our current case this line of code is needed for commands to run.
    # Please check the latest post in this thread for explanation:
    # https://forum.omz-software.com/topic/5684/discord-py-1-2-2-bot-doesn-t-respond-to-commands/
    await bot.process_commands(message)


# Register the command "text".
# To use in discord send a message containing <PREFIX>text (ex. "cp!text" in our current code).
@bot.command()
async def text(ctx):
    # To send it as a file.
    await ctx.send(file=discord.File('uwu.txt'))
    # To send it as a text.
    # await ctx.send(textstuff)

# Run the bot with the token
bot.run("<TOKEN>")
