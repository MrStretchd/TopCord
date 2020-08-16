import requests

class TopXyz:
    def __init__(self, token, bot_id):
        self.token = token
        self.bot_id = bot_id

    def Update(self, guild_count:int, shard_count:int=None):
        if shard_count and guild_count:
            UpdateRequest = requests.post("https://topcord.xyz/api/bot/stats/" + str(self.bot_id), headers={"authorization":self.token}, data={"guilds":guild_count, "shards":shard_count})
            return UpdateRequest
        else:
            UpdateRequest = requests.post("https://topcord.xyz/api/bot/stats/" + str(self.bot_id), headers={"authorization":self.token}, data={"guilds":guild_count, "shards":0})
            return UpdateRequest

    def GetStats(self):
        GetRequest = requests.get("https://topcord.xyz/api/bot/" + str(self.bot_id))
        Stats = GetRequest.json()
        return Stats
    
