import json
import os
import webbrowser

with open('data.json') as data:
    db = json.load(data)

def mode():
    global voice
    voice = True

    mode = input("Hello sir, voice or text?\n")

    if mode.lower() == "voice":
        voice = True

    if mode.lower() == "text":
        voice = False

def translate(text):
    t = r.recognize_google(text)
    t = t.lower()
    return t

def speech(sentence):
    if voice == True:
        engine.say(sentence)
    
    else:
        print(f"Jarvis: {sentence}")

def inquire():
    if voice == True:
        engine.say("I don't know how to respond!") 
        time.sleep(1)
        engine.say("Can you teach me?")

        engine.runAndWait()

        inq = input("You: ")
        engine.say("Thanks! I learnt it now.")

        return inq.capitalize()
    
    else:
        speech("I don't know how to respond! Teach me?")
        inq = input("You: ")
        if inq.lower() == "no":
            speech("No problem! What do you want to talk about?")
            return False
        
        else:
            speech("Thanks! I learnt it now!")
            
            return inq.capitalize()

def ask():
    
    query = input("You: ")
    return query

def search(website):
    website = website.replace(" ", "")
    website = website.lower()
    
    website = website.replace("deepsearch:", "")

    if "https://" not in website:
        website = f"https://{website}/"
        webbrowser.open(f"{website}")

def typo(query):
    query = [*query]
    score = 0
    possible_list = []

    for msg in db:
        msg = [*msg]
        threshold = len(msg) - 4

        for x in query:
            if x in msg:
                if query.index(x) == msg.index(x):
                    score = score + 1
        
        if score >= threshold:
            possible_list.append(msg)
            score = 0
        
        else:
            score = 0

    for x in possible_list:
        if len(x) == len(query):
            x = "".join(x)

            return x
        
    return False
        
