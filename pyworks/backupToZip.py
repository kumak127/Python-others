#! python3
# backupToZip.py - フォルダ全体を連番付きZIPファイルにコピーする

import zipfile, os

def back_up_zip(folder):
    # フォルダ全体をZIPファイルにバックアップする

    folder = os.path.abspath(folder) # フォルダを絶対パスにする

    # 既存のファイル名からファイル名の連番を決める
    number = 1
    while True:
        zip_filename = os.path.basename(folder) + "_" + str(number) + ".zip"    # ファイルの名前は ファイル名_N.zip にする
        if not os.path.exists(zip_filename):                                    # もし -_N.zip というパスがなければ break
            break
        number += 1                                                             # -_N.zip というパスがあるならnumberを増やして再度試す   
    
    # ZIPファイルを生成する
    print(f"Creating {zip_filename}...")
    with zipfile.ZipFile(zip_filename,"w") as backup_zip:                       # フォルダのツリーを渡り歩いてその中のファイルを圧縮する
        for foldername, subfolders, filenames in os.walk(folder):
            print(f"Adding files in {foldername}")                              # 処理中のフォルダ名を表示する
            backup_zip.write(foldername)                                        # 現在のフォルダをZIPに保存する
            for filename in filenames:
                new_base=os.path.basename(folder)+"_"                           # 他のZIPファイルはバックアップしないための処理
                if filename.startswith(new_base) and filename.endswith(".zip"):
                    continue
                backup_zip.write(os.path.join(foldername,filename))             # 現在のフォルダの中の全ファイルをZIPファイルに追加する
    print("Done.")

back_up_zip(input("input File path: "))