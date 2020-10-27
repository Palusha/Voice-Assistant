import playsound
import os
import random


def greetings():
    playsound.playsound("audio/greetings.mp3")


def open_browser():
    os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
    playsound.playsound("audio/open_browser.mp3")


def close_browser():
    os.system('TASKKILL /F /IM  chrome.exe')
    playsound.playsound("audio/close_browser.mp3")


def say_thanks():
    thanks_list = ("you_are_welcome_1", "you_are_welcome_2")
    random_number = random.randint(0, 1)
    playsound.playsound(f"audio/{thanks_list[random_number]}.mp3")


def show_commands():
    playsound.playsound("audio/show_commands.mp3")


def open_asked():
    playsound.playsound("audio/opened_all_u_asked.mp3")


def close_asked():
    pass


def bye():
    playsound.playsound("audio/leave.mp3")
