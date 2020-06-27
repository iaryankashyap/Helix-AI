import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    print("Helix:", audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    speak("I am Helix, How may i help you?")


def take():
    # mic input and returns string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")

        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("You:", query)
    except Exception as e:
        # print(e)
        print("Say that again")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = take().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2)
            speak("According To wikipedia")
            speak(results)
        elif 'open youtube' in query:
            speak("Opening youtube...")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("Opening google...")
            webbrowser.open("google.com")
        elif 'open stack overflow' in query:
            speak("Opening stack overflow...")
            webbrowser.open("stack overflow.com")
        elif 'open stackoverflow' in query:
            speak("Opening stackoverflow...")
            webbrowser.open("stackoverflow.com")
        elif 'open github' in query:
            speak("Opening github...")
            webbrowser.open("github.com")
        elif 'play music' in query:
            musicdir = "C:\\Users\\Aryan\\Music"
            songs = os.listdir(musicdir)
            print(songs)
            os.startfile(os.path.join(musicdir, songs[3]))
            speak("Playing Music...")
        elif 'play songs' in query:
            musicdir = "C:\\Users\\Aryan\\Music"
            songs = os.listdir(musicdir)
            print(songs)
            os.startfile(os.path.join(musicdir, songs[3]))
            speak("Playing Music...")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'visual studio code' in query:
            codepath = "C:\\Users\\Aryan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            speak("Opening V S code...")
