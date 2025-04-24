# Docs:     https://discordpy.readthedocs.io/en/stable/#getting-started
# Tutorial: https://www.youtube.com/watch?v=UCmv8LxF8Xg

from Coinbase import Coinbase
import discord
from discord.ext import commands
import json
import requests

# Open token.txt in read mode, store the reference inside of
# token_file variable
with open('token.txt', 'r') as token_file:
    # Read a single line and store it inside of token
    token = token_file.readline()

# Intents allow the bot to "subscribe" or "listen" to specific events
intents = discord.Intents.all()
# Create an instance of Bot class
bot = commands.Bot(command_prefix='.', intents=intents)

# coinbase gets a reference to a new instance of Coinbase class
coinbase = Coinbase()

"""
Use bot.event() decorator to register an event.

(Event) Callback function - a function that is called
when something happens.

In this case the on_ready() event is called when the bot
has finished logging in and setting things up.
"""
@bot.event
async def on_ready():
    """Called when the bot has finished logging in and
    setting things up."""
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('--------')


# Commands
@bot.command()
async def echo(context: commands.Context, *messages):
    """Repeats a message (or messages) back to the user."""
    separator = ' '
    # Context refers to things like: the user invoking the command, etc.
    await context.send(separator.join(messages))


@bot.command()
async def uselessfact(context: commands.Context):
    """Basic HTTP GET request."""
    # Note: you could improve this by using a Session
    response = requests.get('https://uselessfacts.jsph.pl/random.json')

    if response.status_code == 200:
        json_response = response.json()
        await context.send(json_response['text'])


@bot.command()
async def get_crypto_price(context: commands.Context, *messages):
    if len(messages) != 2:
        await context.send("Usage: .get_crypto_price crypto_currency base_currency")
    else:
        price = coinbase.get_crypto_price(
            currency_pair = {
                "base": messages[1],
                "crypto": messages[0]
            })
        
        if price:
            await context.send(f"{price['amount']:.02f}")
        else:
            await context.send("Usage: .get_crypto_price crypto_currency base_currency")


@bot.command()
async def get_historic_prices(context: commands.Context, *messages):
    if len(messages) != 4:
        await context.send("Usage: .get_historic_prices crypto_currency base_currency start_date end_date")
        await context.send("start_date, end_date: YYYY-MM-DD")
    else:
        historic_prices = coinbase.get_historic_prices({
            "start_date": messages[2],
            "end_date": messages[3],
            "currency_pair": {
                "base": messages[1],
                "crypto": messages[0]
            }
        })
        
        if historic_prices:
            await context.send(json.dumps(historic_prices, indent=4))
        else:
            await context.send("Usage: .get_historic_prices crypto_currency base_currency start_date end_date")
            await context.send("start_date, end_date: YYYY-MM-DD")


# Run the bot with the API token
bot.run(token)
