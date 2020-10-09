#! python3
# spiralDraw.py - ペイントアプリを開き四角い渦の絵を描く

import pyautogui, time, subprocess

subprocess.Popen(r"C:\WINDOWS\system32\mspaint.exe")

pyautogui.moveTo(250,350)   # ペイントの左上らへんに移動する
time.sleep(5)               # 5秒待って、細かい位置は調整してもらう

pyautogui.click()           # ペイントアプリにフォーカスされていない可能性があるので1度クリックする
distance = 500              # 長さをここで変えられる
while distance > 0:         # 長さが0になるまで繰り返す
    pyautogui.dragRel(distance,0, duration=0.05)     # 長さ分右にドラッグする
    distance -= 5                                   # 長さを5短くする
    pyautogui.dragRel(0,distance, duration=0.05)     # 長さ分下に移動する
    pyautogui.dragRel(-distance,0, duration=0.05)    # 長さ分左に移動する
    distance -= 5                                   # 長さを5短くする
    pyautogui.dragRel(0,-distance, duration=0.05)    # 長さ分上に移動する