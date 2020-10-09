#! python3
# multidownloadXkcd.py - XKCDコミックをマルチスレッドでダウンロードする

import requests, os, bs4, threading
os.makedirs("xkcd", exist_ok=True)

def download_xkcd(start_comic, end_comic):
    for url_number in range(start_comic, end_comic):
        # ページをダウンロードする
        print(f"ページをダウンロード中 http://xkcd.com/{url_number}...")
        res = requests.get(f"http://xkcd.com/{url_number}")
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text)

        # コミック画像を見つける
        comic_elem = soup.select("#comic img")
        if comic_elem == []:
            print("画像が見つかりませんでした")
        else:
            comic_url = "http:" + comic_elem[0].get("src")
            # 画像をダウンロードする
            print(f"画像をダウンロード中 {comic_url}...")
            res = requests.get(comic_url)
            res.raise_for_status()

            # 画像を./xkcdに保存する
            with open(os.path.join("xkcd", os.path.basename(comic_url)), "wb") as image_file:
                for chunk in res.iter_content(100000):
                    image_file.write(chunk)

# Threadオブジェクトを生成して開始する
download_threads = []
for i in range(1,1400, 100):
    download_thread = threading.Thread(target=download_xkcd, args=(i, i + 100))
    download_threads.append(download_thread)
    download_thread.start()

for download_thread in download_threads:
    download_thread.join()
print("完了")