#For angry state
import pyttsx3 
import speech_recognition as sr
import heartmain

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

print("1. Exercise")
speak("Exercise")
print("2. Play music")
speak("Play music")
print("3. Open a funny video")
speak("open a funny video")
print("4. open an AudioBook")
speak("open an AudioBook")
print("5. Ask me for a movie recommendation")
speak("Ask me for a movie recommendation")
print("6. Get today's news")
speak("Get today's news")

