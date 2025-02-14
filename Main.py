import threading
import pyautogui
import keyboard
import time
import os

print("Bu program @SilverTeam tarafindan geliştirilmiştir, iyi kullanimlar.\nÇikmak için 'O'-'o' tuşuna basa bilirsiniz.")
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
            print("Program kapatılıyor...")
            os._exit(0) 

thread_q = threading.Thread(target=q_pressed, daemon=True)
thread_q.start()

while True:
    loop()
