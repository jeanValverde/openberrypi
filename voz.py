# pip install gTTS
#pip install playsound

from gtts import gTTS
from playsound import playsound

s = gTTS("respuesta de chat o cualquier cosa")
s.save('sample.mp3')
playsound('sample.mp3')
