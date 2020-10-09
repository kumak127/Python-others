#! python3
# move_file_num.py - 連番ファイルの間に隙間を空けて別の連番ファイルを入れられるようにする

import os, shutil, re
folder_path=os.path.abspath(input(r"検索するフォルダのパス: "))  # フォルダのパス
head_word=input(r"接頭語: ")                                    # 接頭語
wanna_move=int(input("ファイルで空けたい数字: "))                # 連番のファイルで空けたい数字

# 条件に当てはまるファイルを見つけ出す
regex=re.compile(r"^({}.*?)(\d+)(\..*?)$".format(head_word))    # 上の条件に当てはまる正規表現パターン
find_file_list=[]                                               # 条件に当てはまるファイル名のリスト
for foldername, subfolders, filenames in os.walk(folder_path):
    for filename in filenames:
        if regex.search(filename):
            find_file_list.append(filename) # 見つけたファイル名のリスト

# ファイル名のリストから数字部分のみを取り出してリストに入れて反転させる
num_list=[]                                 # ファイル名のリストから数字部分のみを集めたリスト
for file_name in find_file_list:
    re_ob=regex.search(file_name)
    num_len=len(re_ob.group(2))             # 数字の文字数
    num_list.append(int(re_ob.group(2)))    
num_list.reverse()                          # 後ろの数字からずらさないと上書きされてしまうため反転

# ファイル名のリストを反転
find_file_list.reverse()

# 数字の大きいファイルから評価して、ずらす場合は名前を変更
for num, file_na in zip(num_list,find_file_list):       # 数字部分のリストと、ファイル名のリストを入れる
    if num >= wanna_move:                               # 空けたい数字より大きい場合
        num+=1                                          # 数字を+1
        num=str(0)*(num_len-len(str(num)))+str(num)     # ファイルの数字の文字数から、入れる数字の文字数を引いて、余った部分を0で埋める
        re_ob=regex.search(file_na)                     # reオブジェクトを作ってグループごとに分ける
        ch_name=re_ob.group(1) + num + re_ob.group(3)   # 数字の部分を入れる数字に置き換えて、ずらした後のファイル名を入れる
        print(f"{file_na}をずらします")                   
        shutil.move(os.path.join(folder_path,file_na),os.path.join(folder_path,ch_name)) # 名前を変更する

