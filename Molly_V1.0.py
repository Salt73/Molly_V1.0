#!/usr/bin/env python
# coding: utf-8

# In[1]:


# IF YOU DON'T HAVE THOSE LIBRARIES PLEASE RUN PIP STATEMENTS IN THE COMMENT SECTION BELOW
'''
!pip install -q -U google-generativeai    
!pip install speechrecognition openai pyttsx3 pyaudio pygame
!pip install setuptools
'''


# In[ ]:


import google.generativeai as genai
import speech_recognition as sr
import pyttsx3
import os
import pyaudio
from datetime import date
import time
# for OpenAi TTS model you can use
from openai import OpenAi
import pygame
client = OpenAi()


# In[ ]:


pygame.mixeer.init()
today = str(date.today())
engine = pyttsx3.init()
engine.setproperty('rate',190)
voices = engine.getproperty('voices')
engine.setproperty('voice',voices[1].id)# if you want to change it into a male voice replace 1 by 0


# In[ ]:


model=genai.GenerativeModel('gemini-pro')
openaitts = True


# In[ ]:


def speak(text):
    global openaitts
    if openaitts:
        response = client.audio.speech.create(
        model='tts-1',
        voice='nove' # you can replace nova by alloy to switch to a male voice 
        input=text    
        )
        fname = 'output.mp3'
        mp3file = open(fname,'w+')
        response.write_to_file(fname)
        try:
            pygame.mixer.music.load(mp3file)
            pygame.mixer.music.play()
            while(pygame.mixer.music.get_busy()):
                time.sleep(0.25)
            pygame.mixer.music.stop()
            mp3file.close()
            
        except KeyboardInterrupt:
            pygame.mixer.music.stop()
            mp3file.close()
    else:
        engine.say(text)
        engine.runAndWait()


# In[ ]:


talk=[]


# In[ ]:


def append2log(text):
    global today
    fname = 'chatlog-'+today+'.txt'
    with open(fname,"a")as f:
        f.write(text+:"\n")


# In[ ]:


def main():
    global talk, today, model
    rec = sr.Recognizer()
    mic = sr.Microphone()
    rec.dynamic_energy_threshold = False
    rec.energy_threshold = 400
    sleeping = True
    while(1):
        with mic as source1:
            rec.adjust_for_ambient_noise(source1, duration=0.5)
            print("listening...")
            
            try:
                audio = rec.listen(source1, timeout=10, phrase_time_limit = 15)
                text = rec.recognize_google(audio)
                if sleeping == True:
                    if "molly" in text.lower():
                        request = text.lower().split("molly")[1]
                        sleeping = False
                        append2log(f"_"*40)
                        talk=[]
                        today = str(date.today)
                        
                        if len(request) <5:
                            speak("Hi, how can I help you?")
                            append2log(f"AI:Hi, how can I help you? \n")
                            continue 
                    else :
                        continue
                else:
                    request = text.lower()
                    
                    if "that's all" in request:
                        append2log(f"you:{request} \n")
                        speak("Bye")
                        append2log(f"AI:Bye. \n")
                        print("Bye")
                        sleeping = True
                        # AI goes back to sleep
                        continue
                    if "molly" in request:
                        request = request.split("molly")[1]
                append2log(f"you:{request} \n")
                print(f"you:{request}\n AI: ")
                talk.append({'role':'user', 'parts':[request]})
                response = model.generate_content(talk,stream=True)
                for chunk in response:
                    print(chunk.text, end='')
                    speak(chunk.text.replace("*",""))
                    print('\n')
                    talk.append({'role':'model','parts':[response.text]})
                    append2log(f"AI:{response.text} \n")
                except Exception as e:
                    continue


# In[ ]:


if __name__ == "__main__":
    main()

