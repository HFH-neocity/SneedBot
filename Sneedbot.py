#made only to read message history and write messages, simple bot
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
async def video(ctx):
    await ctx.send("https://www.youtube.com/watch?v=zc3vAdsiPV4")
@client.command()
async def janniepost(ctx):
    await ctx.send("Okay. I've fucking had it with this shit. We haven't had a good Simpsons thread in ages and it's time we did something about it. I beg you: mods, janitors and anyone with the power to change this situation. Put pressure on Hiro. Nothing short of a word filter on 'Sneed' will solve this situation.")
@client.command()
async def blue(ctx):
    await ctx.send("YO LISTEN UP HERE'S THE STORY ABOUT A LITTLE GUY THAT LIVES IN THE BASED WORLD AND ALL DAY AND ALL NIGHT AND EVERY THREAD HE SEES IS JUST BASED LIKE HIM INSIDE AND OUTSIDE BASED HIS BOARD, WITH A BASED LITTLE BANEPOST AND A BASED SNEED THREAD AND EVERYTHING IS BASED FOR HIM AND HIMSELF AND EVERY ANON AROUND CUZ HE AINT GOT NO JANNY TO LISTEN TO... I'M BASED IF I WAS CRINGE I WOULD DIE IF I WAS CRINGE I WOULD DIE IF I WAS CRINGE I WOULD DIE IF I WAS CRINGE I WOULD DIE")
client.run("bot token")   
