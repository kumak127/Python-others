#! python3
# stopwatch.py - シンプルなストップウォッチプログラム

import time, threading

# プログラムの説明を表示する
input("Enterを押すと開始します。途中Enterを押すと経過時間を表示します。Ctrl + Cキー で終了します")

start_time = time.time()
print("スタート")
last_time = start_time
lap_num = 1

# ラップタイムを計測する
try:
    while True:
        input()
        now = time.time()
        lap_time = round(now - last_time,2)
        total_time = round(now - start_time,2)
        print(total_time,flush=0.1)
        print("ラップ #{}: {} ({})".format(str(lap_num).rjust(2), str(total_time).rjust(5), str(lap_time).rjust(5)), end="")
        lap_num += 1
        last_time = now
        

except KeyboardInterrupt:
    # Ctrl-C例外を処理してエラーメッセージを表示しないようにする
    print("\n終了")