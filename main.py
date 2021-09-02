import os
import discord
import random
from discord import channel
from discord.ext import commands,tasks
from discord.ext.commands import has_permissions, CheckFailure
import DiscordUtils

client= commands.Bot(command_prefix="+")

#error perms check
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all requirements :rolling_eyes:.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have all the requirements :angry:")

@client.event
async def on_ready():
    print("wholesome iz on the go")
    print("-----------------------------------------")

@client.command()
async def ping(ctx):
     await ctx.send(f'Pong! the best ping is {round(client.latency * 1000)}ms')

#this is the ASK command
@client.command()
async def ask(ctx, *, question):
    responses=["It is certain.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
    response = random.choice(responses)
    embed=discord.Embed(title="here u got the answer!")
    embed.add_field(name='Question: ', value=f'{question}', inline=True)
    embed.add_field(name='Answer: ', value=f'{response}', inline=False)
    await ctx.send(embed=embed)

#this is the HUG command
@client.command()
async def hug(ctx, member):
    author= ctx.message.author.mention
    hugs=["https://c.tenor.com/SPs0Rpt7HAcAAAAM/chiya-urara.gif",
          "https://i.imgur.com/mTAF7zA.gif",
          "https://www.icegif.com/wp-content/uploads/love-hug-icegif.gif",
          "https://i.pinimg.com/originals/8d/ab/29/8dab296aed2cbe25af8ebb4703517356.gif",
          "https://data.whicdn.com/images/45718472/original.gif",
          "https://i.imgur.com/Rez0BKg.gif",
          "https://media1.giphy.com/media/IRUb7GTCaPU8E/giphy.gif",
          "https://c.tenor.com/9e1aE_xBLCsAAAAC/anime-hug.gif",
          "https://thumbs.gfycat.com/ImmaterialHappygoluckyHoneybadger-max-1mb.gif"]
    embed = discord.Embed(title="Hugged", description=f"{author} hugged {member}; aww how cute", color=0xff084a)
    embed.set_image(url= f'{random.choice(hugs)}')
    await ctx.send(embed=embed)

#this is the SLAP command
@client.command()
async def slap(ctx, member):
    author= ctx.message.author.mention
    slaps=["https://c.tenor.com/AzIExqZBjNoAAAAC/anime-slap.gif",
          "https://i.imgur.com/fm49srQ.gif",
          "https://i.imgur.com/9GxTsgl.gif",
          "https://i.gifer.com/9OQv.gif",
          "https://reallifeanime.files.wordpress.com/2014/06/akari-slap.gif",]
    embed1 = discord.Embed(title="Slapped", description=f"{author} slap {member}; got a taste of love", color=0xff084a)
    embed1.set_image(url= f'{random.choice(slaps)}')
    await ctx.send(embed=embed1) 

#this is the RANDGUNVAL command
@client.command()
async def valgun(ctx):
    author= ctx.message.author.mention
    gun=["classic","shorty","frenzy","ghost","sheriff","stinger","spectre","bucky","judge","bulldog","gaurdian","phantom","vandal","marshal","operator","ares","odin"]
    embed2 = discord.Embed(title="here's the gun u should use today", description=f'{author} u should use {random.choice(gun)}', color=0xff084a)
    await ctx.send(embed=embed2)

#this is the kiss command
@client.command()
async def kiss(ctx, member):
    author= ctx.message.author.mention
    kisses=["https://media2.giphy.com/media/bGm9FuBCGg4SY/giphy.gif",
            "https://i2.wp.com/nileease.com/wp-content/uploads/2020/06/0aac390dc598e22578ef476b0f41c0a3.gif",
            "https://c.tenor.com/16MBIsjDDYcAAAAC/love-cheek.gif",
            "https://c.tenor.com/CtpjMGItICQAAAAC/anime-kissing.gif",
            "https://c.tenor.com/-736RHc6hIUAAAAC/anime-kiss.gif",
            "https://c.tenor.com/ErAPuiWY46QAAAAC/kiss-anime.gif"]
    embed3 = discord.Embed(title="Kissed", description=f"{author} kissed {member}; started to make love ❤", color=0xff084a)
    embed3.set_image(url= f'{random.choice(kisses)}')
    await ctx.send(embed=embed3)  

#purge command
@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=5):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount + 1):
              messages.append(message)
    await channel.delete_messages(messages)
    await ctx.send(f'{amount} messages have been purged by {ctx.message.author.mention}')


client.run("ODc5OTI3NzQ2Njg2NTA5MDg4.YSW2kw.jWL1lEK8iQCS6D-NgovkfFUV_ZA")
