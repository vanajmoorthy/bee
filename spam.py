import pyautogui
import time

time.sleep(7)
file = open("beemovie.txt", "r")

for word in file:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
