#Install the library gtts
#write on your command prompt py -m pip install gtts

from gtts import gTTS  #gTTS (Google Text-to-Speech)
import os

user_input = input("Enter the text you want to convert to speech: ")
text_to_speech = gTTS(user_input)

# Save the speech to a file
file_name = "Speak_with_me.mp3"
text_to_speech.save(file_name)

# Play the generated speech
os.system(file_name)


