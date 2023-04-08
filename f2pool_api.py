import requests
import os
import time
import discord_bot

# F2Pool API endpoint URL
API_URL = 'https://api.f2pool.com/bitcoin'

# Define the API request
USER = os.environ['F2POOL_USER']

# Make the API request
response = requests.get(f"{API_URL}/{USER}").json()

for i in range(len(response["workers"])):
    worker = response["workers"][i][0]
    hashrate = response["workers"][i][1]

    print(f"Current hashrate of Miner {worker} = {hashrate/10**12:.1f} TH/s")

discord_bot.run_discord_bot()
