
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
        if "<@botid>" in message.content or ":emojiid:" in message.content or "botname" in message.content or "Botname" in message.content or "botid" in message.raw_mentions:
            reply = response.text
            await message.reply(reply,mention=True)
            #Fill the message content stuff in (there's 2 botnames because one has the name in lowercase and the other with the first letter capiralized). 
            #This is a list of what will cause the bot to reply in this if statement:
            #1 - If you mention/ping the bot in chat. 
            #2 - If you use a specfic emoji.
            #3 - If you say the bot's name in all lowecase.
            #4 - If you say the bot's name with the first letter capitalized.
            #5 - if you reply to one of the bot's messages.

async def main():
    async with aiohttp.ClientSession() as session:
        bot = MyBot(session, "Put your Revolt bot token here.")
        await bot.start()

asyncio.run(main())



