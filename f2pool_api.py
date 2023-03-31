import requests
import os

# F2Pool API endpoint URL
API_URL = 'https://api.f2pool.com/'

# Define the API request
USER = os.environ['F2POOL_USER']

# Make the API request
response = requests.get(f"https://api.f2pool.com/bitcoin/{USER}")

[print(key) for key in response.json().keys()]
print()

hashrate_history = response.json()["hashrate_history"]
worker = response.json()["workers"][0][0]

time, hashrate = list(hashrate_history.items())[-1]
print(f"Current hashrate of Miner {worker} at {time} = {hashrate/10**12:.1f} TH/s")
