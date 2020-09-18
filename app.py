# bot.py
import os

import discord
from dotenv import load_dotenv
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Hi {member.name}, welcome to my Discord server!'
#     )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    spencer_quotes = [
        'Schwing‘ deine Knochen aus meinem Leben!',
        'Alle satt, ja? ‘n Nachschlag gibt’s nicht!',
        'Sein Oberstübchen ist schlecht möbliert!',
        'Gegen meine Kelle hilft nicht mal ein Waffenschein!',
        'Ich musste verschwindibussen!',
        'Schnauze und Ex!',
        'Wenn du denkst, du hast ’nen Dummen vor dir, bist du an der richtigen Adresse!',
        'Mach schon Platz, ich bin der Landvogt!',
        'Ich hab‘ den Nulldurchblick.',
        'Ich glaub‘, mein Tintenfisch kleckert!',
        'Und du machst dir in die Hose und hast nur eine mit, he?',
        'Butter ist Fett, und Fett verklebt die Klumpozipien oder wie das heißt!',
        'Bodybuilding macht nur dicke Knie und Blasen im Hirn!',
        'Ganz ruhig, sonst drücken wir das Köpfchen in deinen Hals.',
        'Ich war schon immer Muttis Heller!',
        'Es ist mir hier zu laut, ich kann nicht richtig kauen!',
        'Hat dir eigentlich schon mal einer mit einem Vorschlaghammer einen Scheitel gezogen?',
        'Mach die Denkmurmel zu!',
        'Locke, ich glaub‘, ich muss dir noch ’nen Satz heiße Ohren verpassen.',
        'Ohne Heu kann das beste Pferd nicht furzen.',
        'Hast du Sodbrennen? Du siehst so sauer aus!',
        'Ich weiß, dass ich ich bin, aber ich weiß nicht, ob du du bist. Weißt du, ob er er ist?',
        'Ein alter Wermut gibt mehr Mut, und Apfelsaft gibt Pokerkraft!',
        'Bisschen Wut ist gut für’s Blut!',
        'Wenn jetzt der Dicke da wäre, würde er euch erstmal die Eierköpfe gradedreschen!',
        'Dem beiß ich ’ne Beule in den Bart, dass dem die Hose wegfliegt!',
        'Zieh‘ gefälligst die Kackstelzen ein!',
        'Ach, äh, Verzeihung, ist das was besonderes, wenn man vier Asse auf der Hand hat?',
        'Von meiner Blutprobe könnten die Bullen ein Betriebsfest machen!',
        'Mhmm, schmeckt garnicht mal so gut!',
        'Ich halte seit hundert Jahren mein Idealgewicht!',
        'Kann ich mir kaum vorstellen, dass es so einen bildschönen, jungen Dynamiker wie mich nochmal gibt.',
        'Dir spitz‘ ich den Spargel an, bis man dich für’n Pfirsich hält!',
        'Nun guck‘ ihn dir an, hat auch nicht mehr Hirn als ’n Spatz Fleisch an der Kniescheibe.',
        'Wiedersehen, aber es eilt nicht!',
        'Ein blindes Huhn trinkt ja auch mal’n Korn!',
        'Wenn du mich nochmal duzt, hau‘ ich dir ’ne Delle in die Gewürzgurke!',
        'Sieht aus wie Bohnen, schmeckt auch wie Bohnen, sind Bohnen!',
        'Hand geb’ ich nicht, kann leicht festkleben!',
        'Mamor, Stein und Eisen bricht, aber mein kleines Fäustchen nicht!',
        'Friedlich wie’n Vulkan!'
    ]

    if message.content == 'mud spencer':
        response = random.choice(spencer_quotes)
        await message.channel.send(response)


client.run(TOKEN)