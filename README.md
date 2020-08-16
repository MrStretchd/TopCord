pip3 install TopCord

```py
from TopCord import TopXyz

TopCord = TopXyz(token=token_here, bot_id=bot_id)

#Update stats
Update = TopCord.Update(guild_count=guild_count, shard_count=optional_shard_count)

#Get stats

Stats = TopCord.GetStats()#Returns a dictionary
```
