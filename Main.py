import threading
import pyautogui
import keyboard
import time
import json
import os

lang = ""

def lang_select():
    global lang
    lang_selec = input("Pls select langs[tr, en, ru]: ")
    lang_ = lang_selec.lower()
    if lang_ == "ru":
        lang = "ru.json"
    elif lang_ == "en":
        lang = "en.json"
    elif lang_ == "tr":
        lang = "tr.json"
    else:
        print("Please select valid language.")
        return lang_select()
    
lang_select()

with open(f"langs/{lang}", "r", encoding="utf-8") as file:
    lang_data = json.load(file)

print(lang_data["creator_message"])
screen_width, screen_height = pyautogui.size()
center_x = screen_width // 2
center_y = screen_height // 2

def loop():
    pyautogui.moveTo(x=center_x, y=center_y)
    pyautogui.press("w")
    time.sleep(1)
    pyautogui.click()
    pyautogui.press("s")

def q_pressed():
    while True:
        if keyboard.is_pressed("o"):
            print(lang_data["progam"])
            os._exit(0) 

thread_q = threading.Thread(target=q_pressed, daemon=True)
thread_q.start()

while True:
    loop()
