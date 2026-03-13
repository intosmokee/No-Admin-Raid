import discord, asyncio
from discord.ext import commands

bt = commands.Bot(command_prefix='/', intents=discord.Intents.all())

@bt.event
async def on_ready():
    await bt.tree.sync() 
    print(f'On {bt.user}')

@bt.tree.command(name='403')
async def spam(i: discord.Interaction):
    await i.response.send_message("on top", ephemeral=True)
    for _ in range(20):
        await i.followup.send("# [Order403 Owns This](https://t.me/ord403)")
        await asyncio.sleep(0.1)

bt.run("") #Your bot token
