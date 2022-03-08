# AI_Chatbot-GPT-3
A GPT-3 AI chatbot with language detect and text-to-speech written in Python <br>

## Requirements
openai <br>
gtts <br>
googletrans==4.0.0rc1 <br>
playsound==1.2.2 <br>
 <br>
## Setup
Create an account on beta.openai.com, and copy the API key under "View API keys", "secret key". <br>
Paste that into the python code where it says "{Enter your openai API key here}". <br>
Make sure to omit the brackets. <br>
 <br>
When installing googletrans and playsound, make sure to use the exact versions as listed in the requirements, as the newer versions are pretty much broken for half the functionality it seems. <br>
 <br>
After typing your own question, the bot will detect whatever language the reponse of the AI is, and convert that to speech. <br>
 <br>
To exit the console, simply ctrl+c out of the program, or close the window.
