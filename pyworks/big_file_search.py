#! python3
# big_file_seach.py - 入力したフォルダの中から大きなファイルデータを探して絶対パスを返す

import os

folder_path=os.path.abspath(input(r"type folder path (ex. C:\Users\user): "))

for foldername, subfolders, filenames in os.walk(folder_path):
    for filename in filenames:
        if 100000000 < os.path.getsize(os.path.join(foldername,filename)):
            print(os.path.join(foldername,filename))