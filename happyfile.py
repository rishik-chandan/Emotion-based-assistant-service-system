#For happy state
import pyttsx3 
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


print("1. say a joke")
speak("say a joke")
print("2. Open a funny video")
speak("open a funny video")
print("3. open an AudioBook")
speak("open an AudioBook")
print("4. Ask me for a movie recommendation")
speak("Ask me for a movie recommendation")
print("5. Exercise")
speak("Exercise")
print("6. Play music")
speak("Play music")
print("7. Get today's news")
speak("Get today's news")