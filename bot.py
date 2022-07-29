from ast import Delete
from configparser import InterpolationSyntaxError
from turtle import title
from unicodedata import name
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import json

intents = discord.Intents.default()
intents.members = True
intents.messages = True



client = commands.Bot(command_prefix= "!", intents=intents)
client.remove_command("help")




#link do bota: https://discord.com/api/oauth2/authorize?client_id=979108610963558400&permissions=8&scope=bot

@client.event
async def on_ready():
    print("|No siema kurwa|")
    print("|Witam w najbardziej zrobionym na odpierdol bocie na ziemii|")
    print("|pozdrawiam merdae|")  
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="jebać toruń!"))




@client.command()
async def help(ctx):
    embed=discord.Embed(title="MOOD", url="https://mood-ssr.vercel.app", description="advertisement sponsored by mood.corp", color=0x4287f5)
    embed.add_field(name="!help", value="pokazuje okienko ktore ci wyskoczylo", inline=False)
    embed.add_field(name="!jebać", value="bot jebie toruń xd", inline=False)
    embed.add_field(name="!Filip", value="opinia na temat Filipa", inline=True)
    embed.add_field(name="!Tomasz", value="zębatka", inline=False)
    embed.add_field(name="!konfident", value="szuka najbliższego konfidenta", inline=False)
    embed.add_field(name="!wojtek", value="fakt związany z Wojteczkiem", inline=False)
    embed.add_field(name="!pykir", value="losowy fakt na temat pykira", inline=False)
    embed.add_field(name="!zuzia", value="niespodzianka...", inline=False)
    await ctx.channel.send(embed=embed, delete_after = 45)
@client.command()
async def Filip(ctx):
    await ctx.channel.send("giga chad")
@client.command()
async def jebać(ctx):
    await ctx.channel.send("jebać toruń")
@client.command()
async def wojtek(ctx):
    await ctx.channel.send("<3")
@client.command()
async def konfident(ctx):
    await ctx.channel.send("sasza i policja jedna koalicja")
@client.command()
async def pykir(ctx):
    await ctx.channel.send("pykir cwel")
@client.command()
async def Tomasz(ctx):
    await ctx.channel.send("odstaw te wódke")
@client.command()
async def XD(ctx):
    await ctx.author.send("XDDDDD")
@client.command()
async def Maria(ctx):
    await ctx.channel.send(":heart:")









