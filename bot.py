import discord
from discord.ext import commands
import os
from model import get_class
IMAGE_DIR = "images"
os.makedirs(IMAGE_DIR,exist_ok=True)
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def hehe(ctx, count_he = 5):
    await ctx.send("he" * count_he)
@bot.command()
async def analiz(ctx):
    if ctx.message.attachments:
        for i in ctx.message.attachments:
            file_name = i.filename
            file_path = os.path.join(IMAGE_DIR, file_name)
            await i.save(file_path)
            await ctx.send("photo reached save point. <3")
            class_name, score = get_class(img=file_path)
            await ctx.send(f"Photo's class: {class_name} Predicted score: {score}%")
            if class_name == 'dog':
                await ctx.send('''How to Feed a Dog
Quality Dog Food: Use foods that contain protein and vitamins.

Meal Routine: Puppies eat 3-4 times a day, adults eat 2 times a day.

Fresh Water: Always keep a bowl of clean water ready.

Dangerous Foods: Never give them chocolate, onions, or cooked bones.''')
            else:
                await ctx.send('''How to Feed a Cat
Meat-Based Diet: Cats need animal protein to stay healthy.

Meal Frequency: You can leave dry food out all day or give small portions.

Wet Food: Give wet food a few times a week to help them get enough water.

Dangerous Foods: Avoid giving them milk (it can hurt their tummy), raw fish, or chocolate.''')
    else:
        await ctx.send("Photo not reached save point. :(  ")
bot.run("TOKEN HERE") 
