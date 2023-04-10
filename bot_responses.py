from f2pool_api import makeRequest

def get_response(message: str) -> str:
    p_message = message.lower()
    
    if p_message == "hello":
        return "Hey there!"
    
    if p_message == "hashrate":
        status = makeRequest()

        message = ""
        for worker in status.keys():
            hashrate = status[worker]["hashrate"]
            message += f"Current hashrate of Miner {worker} = {hashrate:.1f} TH/s\n"

        return message 
    