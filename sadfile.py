#For sad state
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
print("2. Play music")
speak("Play music")
print("3. Ask me for a movie recommendation")
speak("Ask me for a movie recommendation")
print("4. open an AudioBook")
speak("open an AudioBook")
print("5. Exercise")
speak("Exercise")
