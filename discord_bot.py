import os
import asyncio
import discord
import bot_responses as responses
from f2pool_api import makeRequest

DISCORD_BOT_TOKEN = os.environ["DISCORD_BOT_TOKEN"]
DISCORD_CHANNEL_ID = int(os.environ["DISCORD_CHANNEL_ID"])

intents=discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)

async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
        
    except Exception as e:
        print(e)
        
async def send_discord_message(message):
    try:
        channel = client.get_channel(DISCORD_CHANNEL_ID)
        await channel.send(message)
        
    except Exception as e:
        print(e)

async def api_monitor():
    # The interval between API requests in seconds
    interval = 600

    while True:
        status = makeRequest()

        for worker in status.keys():
            if status[worker]["hashrate"] < 1:
                await send_discord_message(f"Warning! Worker {worker} is offline!")
                await send_discord_message(f"Rebooting the system now.")

        # Wait for the specified interval before making the next request
        await asyncio.sleep(interval)

@client.event
async def on_ready():
    print(f"{client.user} is now running")
    await api_monitor()
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)
    
    print(f'{username} said "{user_message}" ({channel})')
    
    if user_message[0] == '?':
        user_message = user_message[1:]
        await send_message(message, user_message, is_private=True)
    else:
        await send_message(message, user_message, is_private=False)

if __name__ == "__main__":
    client.run(DISCORD_BOT_TOKEN)
    