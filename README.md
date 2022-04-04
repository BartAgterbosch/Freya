# Freya
## A GPT-3 AI chatbot with speech-to-text and text-to-speech written in Python <br>

## Requirements
openai <br>
gtts <br>
speech_recognition <br>
googletrans==4.0.0rc1 <br>
playsound==1.2.2 <br>
 <br>
## Setup
Create an account on beta.openai.com, and copy the API key under "View API keys", "secret key". <br>
Paste that into the freya_key.dat file which should be located in the same location as the Freya.exe file. <br>
If that file does not exist and/or cannot be found, it will be created for you. <br>
 <br>
When installing googletrans and playsound, make sure to use the exact versions as listed in the requirements, as the newer versions are pretty much broken for half the functionality it seems. <br>
 <br>
After listening for user input, Freya will parse that to text, and will query openai, the bot will detect whatever language the reponse of the AI is, and convert that to speech. <br>
 <br>
To exit the console, simply ctrl+c out of the program, or close the console window.
