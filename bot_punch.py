import discord
import random
import logging
import json

TOKEN = 'Inscrit son token'

client = discord.Client()

def load_data_from_file(filename):
        try:
            file = open(filename, encoding='utf8')
            data = json.load(file)
            file.close()
            print("Datas loaded")
            return data
        except Exception as e:
            print("Can't load data from " + filename + ", error :")
            logging.exception(e)

listPunch = load_data_from_file("monJson.json") 
listCamillPunch = load_data_from_file("camilleJson.json")
listDarone = load_data_from_file("maman.json")
listPokeman = load_data_from_file("pokeman.json")

@client.event
async def on_ready():
    print('Logged into discord as {} {}'.format(client.user.name, client.user.id))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!help'):
        listCom = [" Liste des Commandes de TYSONPunch ","!lecamille   Poste une punch de Camille "," !punchline    Post une punch aléatoire ","!daronne  Post une punch sur les mamans","!pokeman  Post une pokeManPunch"]
        desc = listCom[0]+"\n\n"+listCom[1]+"\n"+listCom[2]+"\n"+listCom[3]+"\n"+listCom[4]
        embed = discord.Embed(description=desc, color=discord.Colour( 0x274E13)) 

        await message.channel.send('',embed=embed)

    if message.content.startswith('!daronne'):
        punch = random.choice(listDarone)
        embed = discord.Embed(title=punch['description'], description=punch['artist'], color=discord.Colour(0x660000))

        await message.channel.send('', embed=embed)

    if message.content.startswith('!pokeman'):
        punch = random.choice(listPokeman)
        embed = discord.Embed(title=punch['description'], description=punch['artist'], color=discord.Colour(0xE7E766))

        await message.channel.send('', embed=embed)

    if message.content.startswith('!lecamille'):
        punch = random.choice(listCamillPunch)
        desc = punch['artist']+"\n"+punch['album']
        embed = discord.Embed(title=punch['punchLine'], description=desc, color=discord.Colour(0x20124D)) 

        await message.channel.send('', embed=embed)

    if message.content.startswith('!punchline'):
        punch = random.choice(listPunch)
        desc = punch['artist']+"\n"+punch['album'] + ', ' + punch['vote'] + ' votes'
        embed = discord.Embed(title=punch['punchLine'], description=desc, color=discord.Colour(0x211D2D))
        
        await message.channel.send('', embed=embed)

client.run(TOKEN)
