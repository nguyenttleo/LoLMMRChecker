# bot.py
import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands
import datetime
import requests
from html.parser import HTMLParser


class HTMLFilter(HTMLParser):
    text = ""

    def handle_data(self, data):
        self.text += data


load_dotenv()
TOKEN = 'YOUR-TOKEN'
GUILD = 'YOUR-DISCORD-SERVER-NAME'

# empty whatismymmr link
URL = "https://na.whatismymmr.com/api/v1/summoner?name="

client = discord.Client()


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "!mmr " in message.content.lower():
        name = message.content[5:]
        f = HTMLFilter()
        r = requests.get(url=URL + name)
        data = r.json()
        try:
            normal = dict(data)["normal"]["avg"]
            ranked = dict(data)["ranked"]["avg"]
            aram = dict(data)["ARAM"]["avg"]
            summary = data["ranked"]["summary"]
            try:
                f.feed(summary)
                messagesList = f.text.split("MMR")
                await message.channel.send(messagesList[0] + "\n" + "MMR " + messagesList[1])
            except:
                await message.channel.send("Try playing more ranked games.")

            try:
                if str(normal) == "None":
                    await message.channel.send("No normal MMR data avaible. Not enough games played.")
                else:
                    await message.channel.send("Normal MMR: " + str(normal))
            except:
                await message.channel.send("No normal MMR data avaible. Not enough games played.")

            try:
                if str(ranked) == "None":
                    await message.channel.send("No ranked MMR data avaible. Not enough games played.")
                else:
                    await message.channel.send("Ranked MMR: " + str(ranked))
            except:
                await message.channel.send("No ranked MMR data avaible. Not enough games played.")

            try:
                if str(aram) == "None":
                    await message.channel.send("No ARAM MMR data avaible. Not enough games played.")
                else:
                    await message.channel.send("ARAM MMR: " + str(aram))
            except:
                await message.channel.send("No ARAM MMR data avaible. Not enough games played.")

        except:
            await message.channel.send("This summoner does not exist.")

client.run(TOKEN)
