#! python3
# dice_game.py - 多面体のサイコロを振り、数が多いほうが勝つゲーム

import dice
while True:
    num=input('4, 6, 8, 12, 20のどれで勝負しますか？')
    if len(num) == 0:
        break
    num = int(num)
    try:
        my_dice = dice.Dice(num)
        cpu_dice = dice.Dice(num)
    except:
        print('4, 6, 8, 12, 20のどれかを半角数字で入力してください')
        continue
    my_pip = my_dice.shoot()
    cpu_pip = cpu_dice.shoot()
    print('CPU:{} / あなた:{}'.format(cpu_pip, my_pip))
    if my_pip > cpu_pip:
        print('おめでとうございます。あなたの勝ちです！')
    elif my_pip < cpu_pip:
        print('残念...あなたの負けです。')
    else:
        print('引き分けです。')