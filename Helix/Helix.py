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
    global defa
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
        speak("Say Something..")
        defa = "Error"
        return "None"
    defa = "Fine"
    return query


if __name__ == "__main__":
    wishMe()
    mode = "guest"
    os.system('title Helix-AI (GUEST MODE)')
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
            os.startfile(os.path.join(musicdir, songs[3]))
            speak("Playing Music...")
        elif 'play songs' in query:
            musicdir = "C:\\Users\\Aryan\\Music"
            songs = os.listdir(musicdir)
            os.startfile(os.path.join(musicdir, songs[3]))
            speak("Playing Music...")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'visual studio code' in query:
            codepath = "C:\\Users\\Aryan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            speak("Opening V S code...")
        elif 'set color' in query:
            if 'green' in query:
                os.system('color 0A')
                speak('Color set to green.')
            elif 'red' in query:
                os.system('color 0C')
                speak('Color set to red.')
            else:
                speak("Please specify a valid color...")
        elif 'set colour' in query:
            if 'green' in query:
                os.system('color 0A')
                speak('Color set to green.')
            elif 'red' in query:
                os.system('color 0C')
                speak('Color set to red.')
            else:
                speak("Please specify a valid color...")
        elif 'clear' in query:
            if 'screen' in query:
                os.system('cls')
                speak('screen cleared...')
        elif 'terminate' in query:
            speak("terminating code 000")
            break
        elif 'activate administrator mode' in query:
            speak("Please speak your activation code")
            newquery = take()
            if 'zero zero zero' in newquery:
                mode = "admin"
                os.system('cls')
                os.system('color 0A')
                speak("Checking your computer to collect information..")
                speak("Your firewall is activated.")
                speak("Pinging your i p address. please wait...")
                os.system('ping localhost')
                speak("Your computer is connected to the internet.")
                speak("Clearing your screen...")
                os.system('cls')
                speak("Screen cleared..")
                os.system('cls')
                os.system('title Helix-AI (ADMINISTRATOR MODE)')
                speak("Adminstrator mode activated. Welcome Sir.")
            if '0 0 0' in newquery:
                mode = "admin"
                os.system('cls')
                os.system('color 0A')
                speak("Checking your computer to collect information..")
                speak("Your firewall is activated.")
                speak("Pinging your i p address. please wait...")
                os.system('ping localhost')
                speak("Your computer is connected to the internet.")
                speak("Clearing your screen...")
                os.system('cls')
                speak("Screen cleared..")
                os.system('cls')
                os.system('title Helix-AI (ADMINISTRATOR MODE)')
                speak("Adminstrator mode activated. Welcome Sir.")
            else:
                os.system('color 0C')
                speak("Sorry, your activation code is not valid.")
                os.system('color 0F')
        elif 'show' in query:
            if 'network' in query:
                speak("Showing your network. Please wait...")
                os.system('netstat')
                speak("These are the devices connected to you.")
            if 'files' in query:
                os.system('dir')
                speak("These are the files in this directory")
            if 'system configuration' in query:
                os.system('ipconfig')
                speak("This is your system configuration with your i p address")
        elif 'desktop' in query:
            if mode == "admin":
                os.system('cd Desktop')
                os.system('dir')
                speak("These are the files on desktop...")
            else:
                os.system('color 0C')
                speak("Sorry, you are not authorized to perform this action")
        elif 'go back' in query:
            if mode == "admin":
                os.system('cd ..')
                speak("back traversing success")
            else:
                os.system('color 0C')
                speak("Sorry, you are not authorized to perform this action")
        elif "logout administrator" in query:
            mode = "guest"
            os.system('color 0F')
            os.system('title Helix-AI (GUEST MODE)')
            speak("Logged out successfully...")

        else:
            if mode == "admin":
                p = os.system(query)
                if p == 1:
                    os.system('color 0C')
                    speak("Execution Failed")
                if p == 0:
                    os.system('color 0A')
                    speak("Execution success")
            else:
                if defa == "Fine":
                    os.system('color 0C')
                    speak("Not a valid command..")
                    os.system('color 0F')
