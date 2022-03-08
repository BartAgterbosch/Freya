import os
import openai
from time import sleep
from gtts import gTTS
from playsound import playsound
from googletrans import Translator
import tempfile

translate = Translator()

def gpt3(stext):
    openai.api_key = "{Enter your openai API key here}"
    response = openai.Completion.create(
        engine="text-davinci-001",
        prompt=stext,
        temperature=0.6,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6
    )
    content = response.choices[0].text.split(".")
    return response.choices[0].text

try:
    while (True):
        user = input("Jij:")
        response = gpt3(user).lstrip()

        autolang = str(translate.detect(response)).split("=")[1].split(",")[0]
        sentence = gTTS(text=response, slow=False, lang=autolang, tld='nl')
        mp3 = tempfile.NamedTemporaryFile(suffix=".mp3")
        mp3 = mp3.name
        try:
            os.remove(mp3)
        except:
            pass
        sleep(1)
        sentence.save(mp3)
        sleep(1)
        print(f"AI: {response}\n")
        
        playsound(mp3)
        sleep(1)
        try:
            os.remove(mp3)
        except:
            pass
except KeyboardInterrupt:
    pass