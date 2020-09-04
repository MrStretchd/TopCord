# TopCord
The official Python Library for the [topcord.xyz](https://topcord.xyz) website!

# Installation
## Install via pip (Recommended)
```from TopCord import TopXyz```
## Install from source
```
git clone https://github.com/MrStretchd/TopCord
cd TopCord
pip install -r requirements.txt
```

# Examples
## Post stats
With Tasks (Must be using discord.py version 1.1.0+):
```python
import discord, asyncio
from TopCord import TopXyz
from discord.ext import tasks

class TopCord(commands.Cog):
    """Interacts with the TopCord API"""

    def __init__(self, bot):
        self.bot = bot
        self.update_stats.start()
        self.TopCord = TopXyz(token=token)# Make sure you put your token from topcord.xyz here!

    def cog_unload(self):
        self.update_stats.cancel()

    @tasks.loop(minutes=30.0)
    async def update_stats(self):
        """This automatically updates your server count to topcord.xyz every 30 minutes."""
        try:
            await topxyz.post_stats(self.bot.user.id, len(self.bot.guilds))
        except Exception as e:
            print('Failed to post server count to topcord.xyz\n' + type(e).__name__ + ':' + e')

def setup(bot):
    bot.add_cog(TopCord(bot))
```
