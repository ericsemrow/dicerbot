import os
from src.edit_actions import EditActions
from src.rolls import Rolls
from discord.ext import commands

bot = commands.Bot(command_prefix='#')

@bot.listen('on_ready')
async def is_ready():
    print("Online")


bot.add_cog(EditActions(bot))
bot.add_cog(Rolls(bot))


token = os.environ.get("DISCORD_TOKEN")
bot.run(token)