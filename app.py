
import asyncio
import aiohttp
import os
from revolt import Client, Message
from google import genai
from google.genai import types

#https://github.com/revoltchat/revolt.py Revolt API Github
#https://ai.google.dev/gemini-api/docs/quickstart?lang=python Google Gemini API site and docs

#You need the Google Gemini/GenAI API, aiohttp, and Revolt Python API libraries you can get them by using these pip installs. 
#pip install aiohttp
#pip install asyncio
#pip install -q -U google-genai
#pip install revolt.py


client = genai.Client(api_key="Put your Google Gemini API Key here.")

class MyBot(Client):
    async def on_ready(self):
        print(f"Logged in as {self.user.name}")
        #Prints Logged in as (bot name) in your python IDE's console to tell you it's up.

    async def on_message(self, message: Message):
        if message.author.bot:
            return
        #Ignores messages from other bots.

        print(f"Received message: {message.content}")

        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            config=types.GenerateContentConfig(
            system_instruction="Put some instructions for your bot here. As in prompts to tell youe bot about themselves, how to speak, etc. Things you would put in Pesonality, Free Will, AI Engine and Knowledge."), 
            contents=message.content
        )
        reply = response.text
        await message.channel.send(reply)
        #sends a response in the channel, doesn't reply directly to the person messaging them yet.

async def main():
    async with aiohttp.ClientSession() as session:
        bot = MyBot(session, "Put your Revolt bot token here.")
        await bot.start()

asyncio.run(main())



