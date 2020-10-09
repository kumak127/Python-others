#! python3
# resizeAndAddLogo.py - カレントディレクトリのすべての画像を300x300に収まるようにサイズ変更して、catlogo.pngを右下に追加する

import os,re
from PIL import Image

os.chdir(r"..\pydata")

dirname = "withlogo"                    # 管理するフォルダを用意する
os.makedirs(dirname, exist_ok=True)

SQUARE_FIT_SIZE = 300                                   # 画像を収めるサイズを指定する
LOGO_FILENAME = r"..\pydata\catlogo.png"    # ロゴの画像のパス

logo_im = Image.open(LOGO_FILENAME)                     # ロゴImageオブジェクトを生成する
logo_width, logo_height = logo_im.size                  # ロゴのサイズを代入する

extension_list = [".png", ".jpg", ".gif", ".bmp"]          # 処理する拡張子のリスト

# カレントディレクトリの全画像をワープする
for filename in os.listdir("."):
    if filename == LOGO_FILENAME:                       # ファイル名がロゴで使う画像なら飛ばす
            continue 
    for extension in extension_list:                    
        if filename.endswith(extension):                # 処理する拡張子のリストにファイル名が当てはまるなら進む           
            im = Image.open(filename)                           # 見つけた画像のImageオブジェクトを生成する

            # 画像サイズを変更する
            im.thumbnail((SQUARE_FIT_SIZE,SQUARE_FIT_SIZE))     # 画像を指定したサイズ内に収まるようにサイズを変更する
            width, height = im.size                             # 画像の幅と高さを代入する

            if logo_width * 2 > width or logo_height * 2 > height:  # 画像の幅か高さがロゴの倍より小さい場合スキップ
                continue

            # ロゴを追加する
            print(f"ロゴを追加中 {filename}...")
            im.paste(logo_im, (width - logo_width, height - logo_height), logo_im)  # 画像の幅と高さをロゴの幅で引いた位置に貼り付ける(画像の右下)

            # 変更を保存する
            im.save(os.path.join(dirname, filename))            # 管理するフォルダにロゴをつけた画像を追加していく