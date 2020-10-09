#! python3
# countdown.py - シンプルなカウントダウンスクリプト

import time, subprocess

time_left = int(input("秒数を入力してください: "))
while time_left > 0:
    print(str(time_left)+" ", end="\r")
    time.sleep(1)
    time_left -= 1

# カウントダウン後に音声ファイルを再生する
subprocess.Popen(["start", r"..\pydata\Alarm.mp3"], shell=True)