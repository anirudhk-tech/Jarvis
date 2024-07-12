import json
import os
import pyttsx3
import time
import speech_recognition as sr
from func_jarvis import *

query = None
engine = pyttsx3.init()
r = sr.Recognizer()
list_search = ["deepsearch: ", "deepsearch:", "deep search: ", "deep search:"]

engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0")
engine.runAndWait()

mode()

def learn(q, a):
    if a == False:
        pass
    
    else:
        db[q] = a
        with open('new_data.json', "w") as f:
            json.dump(db, f, indent = 2)
        
        os.remove("data.json")
        os.rename("new_data.json", "data.json")

with open('data.json') as data:
    db = json.load(data)


while True:
    query = ask()
    for x in list_search:
        if x in query.lower():
            search(x)
            break
        continue

    
    if query == "exit":
        break
    
    if query == None:
        print("That didn't work")
        speech("Could you repeat that?")
        continue
    
    if query == "clear dict":
        db.clear()

        with open("new_data.json", "w") as f:
            json.dump(db, f)

        
        os.remove("data.json")
        os.rename("new_data.json", "data.json")

        continue
    
    if query not in db:
        check = typo(query)
        
        if check == False:
            inq = inquire()
            learn(query, inq)
            
        else:
            speech(db[check])

    else:
        speech(db[query])


    engine.runAndWait()

