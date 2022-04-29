import discord
from discord.ext import commands
from game import *
from discord_components import DiscordComponents, Button, ButtonStyle
from dotenv import load_dotenv
import os

load_dotenv()

client = discord.Client()

bot = commands.Bot(command_prefix="!", description="THAvalon bot!")
DiscordComponents(bot)
games = {}

@bot.event
async def on_ready():
    print("started")

@bot.command()
async def newgame(ctx):
    
    if ctx.channel.type != discord.channel.ChannelType.text:

        await ctx.channel.send("THAvalon can only be started in a group text channel!")
        return

    if ctx.channel.id in games:

        await ctx.channel.send("A game is already in progress!")
        return

    channel_id = ctx.channel.id

    games[channel_id] = Game()

    await ctx.send(
        "Starting a new game of THAvalon!\n",
        components = [
            Button(label = "Join!", custom_id = "joinbutton")
        ],
    )

@bot.command()
async def list(ctx):

    if ctx.channel.id not in games:

        await ctx.channel.send("No game has been started!")
        return

    player_ids = games[ctx.channel.id].list_players()

    out_str = "Players currently in this game:\n"

    for player_id in player_ids:

        #user = await ctx.guild.fetch_member(player_id)
        out_str += f"<@{player_id}>\n"

    await ctx.channel.send(out_str)

@bot.command()
async def endgame(ctx):

    if ctx.channel.id not in games:

        await ctx.channel.send("No game has been started!")
        return

    await ctx.send(
        "Confirm that you'd like to end the game:\n",
        components = [
            Button(label = "END GAME", custom_id = "endgame")
        ],
    )
    

@bot.event
async def on_button_click(interaction):
    channel_id = interaction.channel.id
    if interaction.custom_id == "joinbutton":
        if not channel_id in games:
            await interaction.respond(content = "No game started!")
            return

        if games[channel_id].has_player(interaction.user.id):
            await interaction.respond(content = "You're already in this game!")
            return

        games[channel_id].add_player(interaction.user.id)
        await interaction.respond(content = "You've joined the game!")
        return

    if interaction.custom_id == "endgame":
        if not channel_id in games:
            await interaction.respond(content = "Game already ended!")
            return

        del games[channel_id]
        await interaction.respond(content = "The game has been ended!", ephemeral = False)

        


    

bot.run(os.getenv("TOKEN"))
    
    
