while True:
    height=input('身長を入力してください(cm or m):')
    if len(height)==0:
        break
    try:
        height=float(height)
    except:
        print('エラー 身長は半角数字で入力してください(cm もしくは m の記入は必要ありません)')
        continue
    try:
        weight=float(input('体重を入力してください(kg):'))
    except:
        print('エラー 体重は半角数字で入力してください(kg の記入は必要ありません)')
        continue
    if height>3:
        height/=100
    bmi=weight/pow(height,2)
    print('あなたのBMI値は{:.2f}です'.format(bmi))
    if bmi<18.5:
        print('あなたはやせ型です')
    elif 18.5<=bmi<25:
        print('あなたは標準体型です')
    elif 25<=bmi<30:
        print('あなたは肥満体型です')
    else:
        print('あなたは高度の肥満体型です')