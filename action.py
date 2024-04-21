import pyttsx3 
import speech_recognition as sr
import datetime
import webbrowser
import os
from GoogleNews import GoogleNews
from detectFaces import label
from joke.jokes import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

print('Detected Emotion....')
print(label)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        print("Good Afternoon!")
        speak("Good Afternoon!")   

    else:
        print("Good Evening!")
        speak("Good Evening!") 
        
    print("I am EBASS. To know your options say HELP")
    speak("I am EBASS. To know your options say HELP")       
   

    
def takeCommand():
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
            
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
 
        query = takeCommand().lower()


        if 'open youtube' in query:
            webbrowser.get(chrome_path).open("youtube.com")

        elif 'open google' in query:
            webbrowser.get(chrome_path).open("google.com")
            
        elif 'movie' in query:
            import movie_rec
            
        elif 'help' in query:
            if label=="Happy" or label=="Neutral":
                import happyfile
            elif label=="Sad":
                import sadfile
            else:
                import angryfile
                
        elif 'exercise' in query:
            print("Opening a exercise video...")
            webbrowser.get(chrome_path).open("https://youtu.be/ml6cT4AZdqI")
            
        elif 'funny video' in query:
            print("Opening a funny video...")
            webbrowser.get(chrome_path).open("https://www.youtube.com/watch?v=GHhFtkGfaWU&list=PLtDp75hOzOlaQcPfx-Za_Dd1sOBPtdBw3")
            
        elif 'joke' in query:
            print("Here is a joke for you")
            speak(geek())
            
        elif 'play audiobook' in query:
            print("Opening an audiobook based on your emotion...")
            if label=="Happy":
                webbrowser.get(chrome_path).open("") #Eyat link laage
            elif label=="Sad":
                webbrowser.get(chrome_path).open("") #Eyat link laage
            else:
                webbrowser.get(chrome_path).open("https://ia903102.us.archive.org/19/items/mindthepaintgirl_1911_librivox/mindthepaint_1_pinero_64kb.mp3")

        elif 'play music' in query:
            print("Playing some happy beats based on your emotion...")
            music_dir = 'C:/Users/ryshi/Music/'+label
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print(f"The time is {strTime}")
            speak(f"The time is {strTime}")
            
        elif 'news' in query:
            print('Searching News...')
            speak('Searching News...')
            googlenews=GoogleNews()
            googlenews=GoogleNews('en','d')
            print('What news would you like to know about?')
            speak('What news would you like to know about?')
            googlenews.search(takeCommand())
            googlenews.getpage(1)
            googlenews.gettext()
            n=(googlenews.gettext())
            print(n)
            #speak(n)
            
        elif 'exit' in  query:
            print("Exiting...")
            speak('Exiting')
            break