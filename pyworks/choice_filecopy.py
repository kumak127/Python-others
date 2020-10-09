#! python
# choice_file_copy -フォルダの中の特定の拡張子を持つファイルをコピーしてcopy_fileという名前のフォルダに収納する

import os, shutil

folder_path=os.path.abspath(input(r"folder path(ex C:\Users\kumak\...): "))  # 参照するフォルダーパス
extension_list=input("search extension(ex .zip .jpeg): ").split()            # コピーする拡張子のリスト
if not os.path.exists(folder_path+"\copy_file"):
    os.mkdir(folder_path+r"\copy_file")                                      # copy_fileという名前のフォルダを作る
copy_file_path=folder_path+r"\copy_file"                                     # copy_fileのパス


# フォルダの中のすべてのファイルを参照して特定の拡張子でファイルが終わっている場合コピーする
for foldername, subfolders, filenames in os.walk(folder_path):               # ディレクトリツリーを渡り歩く
    for filename in filenames:                                                      
        if True in [filename.endswith(extension) for extension in extension_list]:  
            # リスト内包表記を使って拡張子のリストの中に当てはまる拡張子があるかどうか調べる[True,False]という形で返ってくるため True in あるか調べる
            if os.path.exists(os.path.join(copy_file_path,filename)):        # すでにコピー先に同じ名前のファイルがある場合はコピーしない   
                continue  
            shutil.copy(os.path.join(foldername,filename),copy_file_path)    # copy_fileにコピーしす
            print(f"{filename}をコピー")                                      # コピーしたファイル名を表示

print("Done")