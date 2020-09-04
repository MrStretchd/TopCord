import aiohttp, json

class TopXyz:
    def __init__(self, token):
        self.token = token

    async def post_stats(self, bot_id: str, guild_count:int, shard_count:int=None):
        if shard_count is None:
            async with aiohttp.ClientSession() as session:
                async with session.post('https://topcord.xyz/api/bot/stats/' + bot_id,
                headers={'Authorization': str(self.token)},
                data=json.dumps({"guilds": guild_count, "shards": shard_count})) as r:
                    return await r.json()
        else:
            async with aiohttp.ClientSession() as session:
                async with session.post('https://topcord.xyz/api/bot/stats/' + bot_id,
                headers={'Authorization': str(self.token)},
                data=json.dumps({"guilds": guild_count, "shards": 0})) as r:
                    return await r.json()

    async def get_stats(self, bot_id: str):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://topcord.xyz/api/bot/stats/' + bot_id) as r:
                return await r.json()
