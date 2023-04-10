import os
import time
import asyncio
import discord
import threading 
import bot_responses as responses
from f2pool_api import makeRequest

DISCORD_BOT_TOKEN = os.environ["DISCORD_BOT_TOKEN"]
DISCORD_CHANNEL_ID = os.environ["DISCORD_CHANNEL_ID"]

intents=discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
        
    except Exception as e:
        print(e)
        
async def send_discord_message(message):
    channel = client.get_channel(DISCORD_CHANNEL_ID)
    await channel.send(message)

async def api_monitor():
    # The interval between API requests in seconds
    interval = 10

    while True:
        status = makeRequest()

        for worker in status.keys():
            if status[worker]["hashrate"] < 1:
                offline = True
                
        await send_discord_message("Worker offline!")

        # Wait for the specified interval before making the next request
        time.sleep(interval)
           
@client.event
async def on_ready():
    global channel
    channel = client.get_channel(DISCORD_CHANNEL_ID)
    print(f"{client.user} is now running")
    
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
    # Start monitoring thread
    monitor_loop = asyncio.get_event_loop()
    monitor_loop.create_task(api_monitor())
    
    # monitor_thread = threading.Thread(target=api_monitor)
    # monitor_thread.start()
    
    client.run(DISCORD_BOT_TOKEN)
    