import discord
from discord.ext import commands
#prefix
client = commands.Bot(command_prefix=">")
#da commands
@client.event
async def on_ready():
    print("Bot Is Prepared To Sneed.")
@client.command()
async def sneed(ctx):
    await ctx.send("Feed And Seed")
@client.command()
async def applebottomsneeds(ctx):
    await ctx.send("https://tenor.com/view/sneed-formerly-chucks-sneeds-low-boots-with-a-fur-gif-15107941")
@client.command()
async def chuck(ctx):
    await ctx.send("Fuck And Suck")
@client.command()
async def forced(ctx):
    await ctx.send("Sneed.")
@client.command()
async def commandlist(ctx):
    await ctx.send("prefix > | commands: sneed, chuck, applebottomsneeds, forced, commandlist, sneedcat")
@client.command()
async def jelq(ctx):
    await ctx.send("https://www.youtube.com/watch?v=65JF4OT63i8")
@client.command()
async def sneedcat(ctx):
    await ctx.send("https://tenor.com/view/sneed-cat-based-nae-nae-dancing-dance-gif-16884764")