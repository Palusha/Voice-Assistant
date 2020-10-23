import os
import time
import speech_recognition as sr
import playsound
from gtts import gTTS


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


playsound.playsound("audio/greetings.mp3")


while True:
    text = get_audio().lower()

    if "привет" in text:
        playsound.playsound("audio/greetings.mp3")
    elif "открой браузер" in text:
        try:
            os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
            playsound.playsound("audio/open_browser.mp3")
        except Exception as e:
            print('Exception: ' + str(e))
    elif "закрой браузер" in text:
        try:
            os.system('TASKKILL /F /IM  chrome.exe')
            playsound.playsound("audio/close_browser.mp3")
        except Exception as e:
            print('Exception: ' + str(e))
    elif "пока" in text:
        playsound.playsound("audio/already_leaving.mp3")
        playsound.playsound("audio/eh_okay.mp3")
        break
