import os
import time
import speech_recognition as sr
import playsound
from gtts import gTTS
import random
from assistant_commands import *


playsound.playsound("audio/greeting_show_commands.mp3")
commands_dict = {"привет": greetings, "открой браузер": open_browser,
                 "закрой браузер": close_browser, "открой": open_asked,
                 "закрой": close_asked, "спасибо": say_thanks,
                 "команды": show_commands, "пока": bye}


def speak(text):
    tts = gTTS(text=text, lang="ru")


def get_audio():
    r = sr.Recognizer()

    with sr.Microphone(device_index=1) as source:
        print("Скажите что-нибудь")
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio, language="ru")
            print("Вы сказали: " + said.lower())
        except Exception as e:
            print('Exception: ' + str(e))

    return said


text = ""

while text != "пока":
    text = get_audio().lower()
    for name, event in commands_dict.items():
        if name in text:
            try:
                event()
                break
            except Exception as e:
                print('Exception: ' + str(e))
