# https://www.geeksforgeeks.org/convert-text-speech-python/
# Import the required module for text 
# to speech conversion
from gtts import gTTS

# Import pygame for playing the converted audio
import pygame

# The text that you want to convert to audio
mytext = 'La investigación de los mayores desafíos terrestres, tanto ambientales como científicos y sociales, recae en manos de los geocientíficos. Sin embargo, y a pesar de sus incansables esfuerzos, grandes misterios como el origen de la Tierra y de la vida misma continúan sin resolverse.'

# Language in which you want to convert (en/es)
language = 'es'

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("tarea.mp3")

# Initialize the mixer module
pygame.mixer.init()

# Load the mp3 file
pygame.mixer.music.load("welcome.mp3")

# Play the loaded mp3 file
pygame.mixer.music.play()