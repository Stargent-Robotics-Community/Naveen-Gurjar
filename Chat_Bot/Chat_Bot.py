#!/usr/bin/env python
# coding: utf-8

# In[1]:


#This is a basic chat bot which will recommend movies or anime according to the genre specified by the user 


# In[2]:


import datetime


# In[3]:


import pyttsx3 as pts


# In[4]:


engine = pts.init()


# In[5]:


def speak(input):
    engine.say(input)
    engine.runAndWait()


# In[6]:


import speech_recognition as sr


# In[7]:


r = sr.Recognizer()


# In[8]:


def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold=1
        print("Microphone is started, please speak")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language ='en-in')
            print(text)
        except:
            print("please speak again")
        return text    


# In[9]:


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning!")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon!")  
  
    else:
        speak("Good Evening!")


# In[10]:


wishMe()
speak("How are you")


# In[11]:


speak("What would you like to watch")
speak("Animation or Movie")
print("Animation or Movie")
#I mean anime but I couln't use it because the term anime was getting recognised as animal, so I used the alternative.
category = listen().lower()


# In[12]:


speak("What genre do you want to watch")
#chose from the following genres:
#Movie : Science Fiction, Comedy, Action, Horror
#Anime : Thriller, Isekai, Comdey, Shounen, Sports, Slice of Life
genre = listen().lower()


# In[13]:


print("Here is a list of recommendations:")
speak("Here is a list of recommendations")

if category == "movie" and genre == "science fiction":
    print("Interstellar \nGravity \nThe Martian \nReady Player one")
    speak("Interstellar, Gravity, The Martian, Ready Player one")
    speak("Hope you like them")

elif category == "movie" and genre == "comedy":
    print("The Hangover \nGrown Ups \nWhy Him \nThe Dictator")
    speak("The Hangover, Grown Ups, Why Him, The Dictator")
    speak("Hope you like them")

elif category == "movie" and genre == "action":
    print("Jhon Wick \nThe Expandables \nBad Boys \nG I Joe")
    speak("Jhon Wick, The Expandables, Bad Boys, I Joe")
    speak("Hope you like them")

elif category == "movie" and genre == "horror":
    print("The Conjuring \nAnnabelle \nIT \nThe Nun")
    speak("The Conjuring, Annabelle, IT, The Nun")
    speak("Hope you like them")

elif category == "animation" and genre == "thriller":
    print("Death Note \nPsycho Pass \nAttack on titan \nCode Geass")
    speak("Death Note, Psycho Pass, Attack on titan, Code Geass")
    speak("Hope you like them")

elif category == "animation" and genre == "isekai":
    print("The time I got reincarnated as slime \nOverlord \nJobless Reincarnation \nThe Rising of Shield hero")
    speak("The time I got reincarnated as slime, Overlord, Jobless Reincarnation, The Rising of Shield hero")
    speak("Hope you like them")
    
elif category == "animation" and genre == "comedy":
    print("Grand Blue \nKonosuba")
    speak("Grand Blue, Konosuba")
    speak("Hope you like them")

elif category == "animation" and genre == "shounen":
    print("Naruto \nOne Piece \nHunter X Huntern \nBlack Clover")
    speak("Naruto \nOne Piece \nHunter X Huntern \nBlack Clover")
    speak("Hope you like them")
    
elif category == "animation" and genre == "sports":
    print("Haikyuu \nKuroko No Basuke")
    speak("Haikyuu, Kuroko No Basuke")
    speak("Hope you like them")
    
elif category == "animation" and genre == "slice of life":
    print("Horimiya \nTsuki Ga Kire \nOrange \nJust Because")
    speak("Horimiya, Tsuki Ga Kire, Orange, Just Because")
    speak("Hope you like them")

