#! python3
# randomQuizeGenerator - ランダムに問題と答えを並べ替え問題集と回答集を作る

import random, re, os

# 問題のデータ キーが都道府県で、値が県庁所在地
with open(r"..\pydata\県庁所在地_一覧.txt", encoding="utf-8") as f:
    data = f.read()                       # 県庁所在地の一覧のテキストを入手
rm_regex = re.compile(r"\d|(\(.*?\))")    # 数字と()内のフリガナをパターンにする
clear_data = rm_regex.sub("", data)        # 数字と()内のフリガナを削除(空文字に変換)
sp_regex = re.compile(r"\n+")             # 1個以上の改行(\n)をパターンにする
ken_shi_list = sp_regex.split(clear_data) # 改行ごとに区切ったリストを作る
ken_list = ken_shi_list[0::2]             # 奇数番目は県なのでスライスして奇数のリストを変数に
shi_list = ken_shi_list[1::2]             # 偶数番目は市なのでスライスして偶数のリストを変数に
capitals = {}                             # 県庁所在地のデータを入れる空の辞書を作成
for ken, shi in zip(ken_list, shi_list):  # zipを使ってキーが都道府県、値が県庁所在地の辞書を作る
    capitals[ken] = shi

# 35個の問題集を作成する
os.mkdir(r"..\pydata\quiz_folder")

for quiz_num in range(35):
    # 問題集と回答集のファイルを作成する
    quiz_file = open(r"..\pydata\quiz_folder\capitalsquiz{}.txt".format(quiz_num+1), "w")
    answer_key_file = open(r"..\pydata\quiz_folder\capitalsquiz_answer{}.txt".format(quiz_num+1), "w")

    # 問題集のヘッダーを書く
    quiz_file.write("名前:\n\n日付:\n\n学期:\n\n")
    quiz_file.write((" 　　　　") + "都道府県県庁所在地クイズ(問題番号 {})".format(quiz_num + 1))
    quiz_file.write("\n\n")

    # 都道府県の順番をシャッフルする
    prefectures = list(capitals.keys())                         # 都道府県のリストを作る
    random.shuffle(prefectures)                                 # 都道府県のリストをシャッフル
    
    # 47都道県をループして、それぞれの問題を作成する
    for question_num in range(len(prefectures)):                # 都道府県の数だけ繰り返す
        # 正解と誤答を取得する
        correct_answer = capitals[prefectures[question_num]]    # 都道府県の名前(キー)を使ってそ正解の県庁所在地をcollect_answerに入れる
        wrong_answers = list(capitals.values())                 # 県庁所在地の入ったリストwrong_answersを作る
        del wrong_answers[wrong_answers.index(correct_answer)]  # 県庁所在地のリストから正解の県庁所在地を削除する
        wrong_answers = random.sample(wrong_answers, 3)         # 県庁所在地のリストから3つをランダムに選び、wrong_answersを上書きする(リスト)
        answer_options = wrong_answers + [correct_answer]       # wrong_answersのリストと正解のcorrect_answerをリスト(answer_options)にして結合する
        random.shuffle(answer_options)                          # 回答の選択肢の並びをシャッフルする

        # 問題文と回答選択肢を問題ファイルに書く
        quiz_file.write("{}.{}の都道府県庁所在地は？\n".format(question_num + 1, prefectures[question_num]))    # 問題文を書く
        for i in range(4):
            quiz_file.write(" {}.{}\n".format("ABCD"[i], answer_options[i]))                                   # 選択肢を書く 
        quiz_file.write("\n")

        # 答えの選択肢をファイルに書く
        answer_key_file.write("{}.{}\n".format(question_num + 1, "ABCD"[answer_options.index(correct_answer)]))# 答えの選択肢を書く
    
    quiz_file.close()
    answer_key_file.close()