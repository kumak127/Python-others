#! python3
# correct_file_number.py - 指定した接頭語に続くファイル名の連番に飛んでいる数字がないか調べ、あった場合ずらして、正しく並べ替える

import os, shutil, re

folder_path = input(r"連番を整理するフォルダーのパスを入れてください: ")  # 整理するフォルダのパス
head_word = input(r"接頭語があれば入力してください: ")                   # 接頭語 
regex = re.compile(r"^({}.*?)(\d+)(\..*$)".format(head_word))          # 上の条件に合う正規表現のパターン

# 条件に当てはまるファイルを見つけ出す
file_number_list = []                                             # 条件に当てはまったファイル名の数字を入れるリスト
correct_file_path_list = []                                       # 条件に当てはまったファイルの絶対パスを入れるリスト
for foldername, subfolders, filenames in os.walk(folder_path):  # ディレクトリの全ファイルを参照
    for filename in filenames:
        if regex.search(filename):                              # ファイル名が正規表現のパターンに当てはまるなら
            correct_file = regex.search(filename)                 # ファイル名のreオブジェクトを作成
            file_number_list.append(correct_file.group(2))      # 条件に当てはまった数字のリストに、数字の部分のみを入れる(str型)
            num_len = len(correct_file.group(2))                  # 数字の文字数を入れる
            correct_file_path_list.append(os.path.join(foldername, filename)) # 条件に当てはまったファイルの絶対パスのリスト

# 数字が連番になっている場合のリストを作る
search_num=1
correct_number_list=[] # 正しい数字の並びのリスト(int型)
for num in file_number_list:
    if int(num) == 0:  # 数字が0で始まっている場合
        correct_number_list.append(int(num))
    else: 
        correct_number_list.append(search_num)
        search_num += 1

# ファイルの名前を変える
for file_path, correct_num in zip(correct_file_path_list, correct_number_list):  # 条件にあてはまったファイルの絶対パスと正しい並びの数字を変数に入れる
    dirname, file_name = os.path.split(file_path)                 # ファイルの絶対パスをディレクトリのパスとファイル名に分ける
    match_ob = regex.search(file_name)                            # reオブジェクトを作って、
    a, b, c = match_ob.groups()                                     # 数字の前までの名前、数字の部分、数字の後の名前に分ける
    b = str(0) * (num_len - len(str(correct_num))) + str(correct_num)   # 一番多い数字の文字数から、今処理している数字の文字数を引いて、その数字分の0で埋める。そのあと、正しい数字を足す
    correct_file_name = a + b + c                                     # 正しいファイル名を作る
    print(f"{file_path}を{correct_file_name}に変更しました")
    shutil.move(file_path, os.path.join(dirname, correct_file_name))  # 処理前のファイル名を、正しいファイル名に変更する
    
    

    
    