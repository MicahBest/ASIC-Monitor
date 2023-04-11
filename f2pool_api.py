import requests
import os

def makeRequest():
    # Define the API request
    API_URL = 'https://api.f2pool.com/bitcoin'
    USER = os.environ['F2POOL_USER']

    # Make the API request
    response = requests.get(f"{API_URL}/{USER}").json()
    
    info = {}

    for i in range(len(response["workers"])):
        worker = response["workers"][i][0]
        hashrate = response["workers"][i][1]/10**12
        
        info[worker] = {}
        info[worker]["hashrate"] = round(hashrate, 1)

    return info