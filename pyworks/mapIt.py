#! python3
# mapIt.py - コマンドラインやクリップボードに指定した住所の地図を開く

import webbrowser, sys, pyperclip
if len(sys.argv) >1:
    # コマンドラインから住所を取得する
    address = " ".join(sys.argv[1:])

# クリップボードから住所を取得する
else:
    adress = pyperclip.paste()

webbrowser.open("https://www.google.com/maps/place/"+ address)