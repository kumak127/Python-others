#! python3
# downloadXkcd.py - XKCDのコミックをひとつづダウンロードする

import requests, os, bs4

url = "http://xkcd.com"                                     # XKCDコミックのURL
os.makedirs(r".\xkcd", exist_ok=True)    # 保存するディレクトリを作る(exist_okは既に存在するときにエラーを起こさないためのキーワード)
while not url.endswith("#"):                                # prevで最後まで行ったときのURLのおわりが＃なので、最後まで行ったらループを抜け出す 
    # ページをダウンロードする
    print(f"ページをダウンロード中 {url}...")
    res = requests.get(url)                                 # requests.get でページをダウンロード
    res.raise_for_status()                                  # raise_for_status でダウンロードに失敗したらエラーを起こして終了

    soup = bs4.BeautifulSoup(res.text)                      # BeautifulSoupオブジェクトを作成

    # コミック画像のURLを見つける
    comic_elem = soup.select("#comic img")                  # 画像の<img>要素はidがcomicの<div>要素の中にあるのでセレクタを使って内容を取得
    if comic_elem == []:                                     # 要素が見つからなかった場合の処理
        print("コミック画像が見つかりませんでした")
    else:
        comic_url = "http:" + comic_elem[0].get("src")      # <img>要素からURLの内容が入っているsrcを指定してhttp:と文字列を足す
        # 画像をダウンロードする
        print(f"画像をダウンロード中 {comic_url}...")
        res = requests.get(comic_url)                       # 画像をダウンロード
        res.raise_for_status()                              # 画像のダウンロードに失敗したらエラーを起こして終了

        # 画像をxkcdに保存する
        with open(os.path.join(r".\xkcd", os.path.basename(comic_url)), "wb") as image_file:
            for chunk in res.iter_content(100000):          # 変数resにダウンロードされている画像データをiter_contentで100kbずつファイルに保存する
                image_file.write(chunk)
        
    # prevボタンのURLを取得する
    prev_link = soup.select("a[rel='prev']")[0]             # <a>の中のrel属性がprevの値である要素を取得
    url = "http://xkcd.com" + prev_link.get("href")         # <a>の中のhref属性から前ページのURLを取得して変数を変更してwhileループを繰り返す

print("ダウンロード終了")