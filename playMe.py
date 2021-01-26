import asyncio
import discord
from discord.ext import commands, tasks
import os
from random import choice
from keep_alive import keep_alive
import requests
import json

client = commands.Bot(command_prefix='.')

status = ['listening music !', 'eating !', 'sleeping !', ' music for you !']

waves = [
    '***waving you back 👋***', 'why did you wake me up ? 🥱',
    'pls, let me sleep 💤', '💤 am sleeping, do not disturb',
    'wanna let me play some music for you ? 🎶', 'whatssup ? dude !! ;)'
]

die = [
    'what wrong have I done to you ?', 'why do you want to kill me ?',
    '**sabotage** activated !!', '***omae wa mou shindeiru*** 😈',
    'I have such a small life, you want that too ?', '***DEAD***',
    '**RIP** me', 'you are accused of `Attempt To Murder`'
]

good_morning = [
    'Good morning to you. May every step you make be filled with happiness, love, and peace.',
    'May this morning offer you new hope for life! May you be happy and enjoy every moment of it. Good morning!',
    'Good morning! May your day be filled with positive things and full of blessings. Believe in yourself.',
    'Good Morning my love! I hope my good morning text will bring a smile on your face at the very beginning of the day. I love you so much.',
    'Every morning is a new blessing, a second chance that life gives you because you’re so worth it. Have a great day ahead. Good morning!',
    'Get up early in the morning and don’t forget to say thank you to God for giving you another day! Good morning!',
    'Good morning, my friend! Life gives us new opportunities every day, so hoping today will be full of good luck and prosperity for you!',
    'Good Morning, dear! May everything you dreamed about last night comes true!',
    'Good morning. I hope you have a wonderful day.',
    'Life never gives you a second chance. So, enjoy every bit of it. Why not start with this beautiful morning. Good morning!',
    'Life is full of uncertainties. But there will always be a sunrise after every sunset. Good morning!'
]

good_night = [
    'good night, have sweet dreams',
    'Hey there, just dropped by to say hello. Hope that you had a wonderful day! Good Night!',
    'I couldn’t fall asleep unless I told you how much I miss you – love you and goodnight!',
    'Today has been a non-stop, hectic, crazy day, and I wish I had gotten time to see you… so I’m thinking about U before I fall asleep. Goodnight, sleep tight!',
    'We are together for a very long time now, and I just wanna let you know that I love you more than ever now. Good Night',
    'I don’t know what I’d do without you. You mean everything to me. Good Night.',
    'One day I wish my dream would come true, And I’d wake up next to you. Till then Good Night!',
    'When I sleep, it is a call to you and when I dream it is a wait for U. Good Night.',
    'Sleep tight and good night as I wish you the best of dreams with all of my might.',
    ' I know I will have sweet dreams tonight, my only nightmares are when U are away from me. Have a lovely night.',
    ' While the moon is shining in the sky, you are the brightest star of my night. Good Night.'
]

# love_words = ['i love you', 'love', 'luv', 'lub', '❤']

# love_reply = ['love you too ❤️', 'love you 2 ❤️', '❤️ you too...']


@client.event
async def on_ready():
    change_status.start()
    print('Bot is Online !')


@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='welcome')
    await channel.send(
        f'Welcome {member.mention}!  Ready to jam out? See `?help` command for details!'
    )


@client.command(
    name='ping', help='this command will return you with Latency !')
async def ping(ctx):
    await ctx.send(
        f'**pinged !** Latency is : {round(client.latency * 1000)}ms')


@client.command(name='hello', help='this command will wave you back !')
async def waving(ctx):
    await ctx.send(choice(waves))


@client.command(name='die', help='this command will kill you or someone !')
async def dead(ctx):
    await ctx.send(choice(die))


@client.command(
    name='goodMorning',
    help='this command will greet you with good morning wishes!')
async def goodMorning(ctx):
    await ctx.send(choice(good_morning))


@client.command(
    name='goodNight',
    help='this command will greet you with good night wishes!')
async def goodNight(ctx):
    await ctx.send(choice(good_night))


@tasks.loop(hours=1)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))

#-----------------------------------------------------------
def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' -' + json_data[0]['a']
    return quote


@client.command(name='quotes', help='this command will send some quotes')
async def send_msg(ctx):
    quote = get_quote()
    await ctx.send(quote)
#-----------------------------------------------------------

@client.command(name='clear', help='this command will clear msgs')
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit=amount)



# @client.command()
# async def send_msg(ctx):
#   msg = message.content
#   if any(word in msg for word in love_words):
#     await ctx.send(choice(love_reply))
    

keep_alive()

client.run(os.getenv('TOKEN'))



