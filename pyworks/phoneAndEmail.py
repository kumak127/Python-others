#! python3
# phoneAndEmail.py - 海外の電話番号やメールアドレスをクリップボードから探し出し、クリップボードにコピーする

import re, pyperclip
# 電話番号の正規表現を作る
phone_regex = re.compile(r"""(
    (\d{3}|\(d{3}\))?               # 市外局番
    (\s|-|\.)?                      # 区切り
    (\d{3})                         # 3桁の番号
    (\s|-|\.)                       # 区切り
    (\d{4})                         # 4桁の番号
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # 内線番号
    )""", re.X)

# 電子メールの正規表現を作る
email_regex = re.compile(r"""(
    [a-zA-Z0-9._%+-]+   # ユーザー名
    @                   # @記号
    [a-zA-Z0-9.-]+      # ドメイン名
    (\.[a-zA-Z]{2,4})   # ドットなんとか
    )""", re.X)

# クリップボードのテキストを検索する
text=str(pyperclip.paste())
matches=[]
for groups in phone_regex.findall(text):
    phone_num = "-".join([groups[1], groups[3], groups[5]])
    if groups[8] != "":
        phone_num += " x" + groups[8]
    matches.append(phone_num)
    for groups in email_regex.findall(text):
        matches.append(groups[0])

# 検索結果をクリップボードに貼り付ける
if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("クリップボードにコピーしました")
    print("\n".join(matches))
else:
    print("電話番号やメールアドレスは見つかりませんでした")