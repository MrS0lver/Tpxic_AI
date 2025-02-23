import speech_recognition as sr
import pyttsx3 as pt
import google.generativeai as genai
import shutil
import os
import threading
import itertools
import sys
import time
from AppOpener import open, close
import subprocess
import urllib.request
import webbrowser as web

genai.configure(api_key="AIzaSyDC5nfuYOHVc-eZeg1rYeS04OdsAhXFvIA")
model = genai.GenerativeModel("gemini-1.5-flash")

def say(text):
    engine = pt.init()
    engine.setProperty('rate', 165)
    engine.say(text)
    engine.runAndWait()

def listen():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        rec.adjust_for_ambient_noise(source)
        audio = rec.listen(source)
        try:
            print("Recognizing....")
            data = rec.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            return "Try AGAIN!"
        except sr.RequestError as e:
            return f"Could not request results; {e}"

def loading_animation(stop_event):
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if stop_event.is_set():
            break
        sys.stdout.write(f'\r... {c}')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r')
    sys.stdout.flush()

class Main:
    def voice(self):
        print("Voice Mode Activated!")
        while True:
            try:
                user_input = listen()
                print(f"You said: {user_input}")
                stop_event = threading.Event()
                loader = threading.Thread(target=loading_animation, args=(stop_event,))
                loader.start()
                response = model.generate_content(f"generate answer very toxic and angry, dont generate very long answer! {user_input}")
                stop_event.set()
                loader.join()
                print(response.text)
                say(response.text)
                if "stop" in user_input:
                    break
            except Exception as e:
                print(f"An error occurred: {e}")
        print("Voice Mode Deactivated!")

    def set1(self):
        print("Quick Start Activated!")
        startup_folder = os.path.join(os.getenv("APPDATA"), "Microsoft\\Windows\\Start Menu\\Programs\\Startup")
        script_path = os.path.abspath(__file__)
        destination_path = os.path.join(startup_folder, os.path.basename(script_path))
        try:
            shutil.move(script_path, destination_path)
            print(f"Script copied to startup: {destination_path}")
        except Exception as e:
            print(f"Failed to copy script: {e}")

    def Sp1(self):
        print("This Feature is Not Available Yet (Developing ...!)")

    def SrcFile(self, filename):
        search_path = os.path.expanduser("~")
        found_files = []
        
        for root, dirs, files in os.walk(search_path):
            if filename in files:
                found_files.append(os.path.join(root, filename))
        
        if found_files:
            print(f"File '{filename}' found at:")
            for file in found_files:
                print(file)
        else:
            print(f"File '{filename}' not found.")

func = Main()
operation = {
    "V1": func.voice,
    "Set1s": func.set1,
    "dc": lambda: open("Discord"),
    "wp": lambda: open("whatsapp"),
    "code": lambda: open("vscode"),
    "OFF0": lambda: os.system("shutdown /s /t 0.5"),
    "ON1": lambda: os.system("shutdown /r /t 0"),
    "Sp1": func.Sp1,
    "ScF3": func.SrcFile,
    "InsTA": lambda: web.open("https://www.instagram.com/"),
    "TwiTx": lambda: web.open("https://x.com/home"),
    "YT0": lambda: web.open("https://www.youtube.com/"),
}

while True:
    inp = input("--> ")
    if inp in operation.keys():
        operation.get(inp, lambda: print("Invalid operation. Please enter a valid command."))()
    elif inp.startswith("S3 "):
        url = inp[3:].strip()
        if not url.startswith("http"):
            url = "https://www.google.com/search?q=" + url.replace(" ", "+")
        web.open(url)
    elif "ScF3" in inp:
        operation["ScF3"] = lambda: SrcFile(input("--> Enter filename to search: ").strip())
    else:
        try:
            stop_event = threading.Event()
            loader = threading.Thread(target=loading_animation, args=(stop_event,))
            loader.start()
            response = model.generate_content(f"generate answer very toxic and angry, dont generate very long answer! {inp}")
            stop_event.set()
            loader.join()
            print(response.text)
        except Exception as e:
            print(f"An error occurred: {e}")
