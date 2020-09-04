import aiohttp

class TopXyz:
    def __init__(self, token):
        self.token = token

    async def post_stats(self, bot_id, guild_count:int, shard_count:int=None):
        if shard_count is None:
            shard_count = 0
        async with aiohttp.ClientSession() as session:
            async with session.post('https://topcord.xyz/api/bot/stats/' + str(bot_id),
            headers={'Authorization': str(self.token)},
            data={"guilds": guild_count, "shards": shard_count}) as r:
                return await r.json()

    async def get_stats(self, bot_id):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://topcord.xyz/api/bot/' + str(bot_id)) as r:
                return await r.json()
