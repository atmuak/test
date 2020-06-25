import random
import math

hand = ["グー", "チョキ", "パー"]

print('ジャンケンゲームを始めます')
print('0:グー、1:チョキ、2:パーです')

score = 0
count = 0

user_hand = int(input("出す手を数値で入力:"))
cpu_hand = random.randint(0, 2)

print('あなたの手は' + hand[user_hand] + 'です')
print('コンピュータの手は' +hand[cpu_hand] + 'です')

while True:
    try:
        if count > 0:
            win = math.floor(score / count * 100)
            print(count, "戦目")
            print("スコア：", score, "/", count)
            print("　勝率：", win)
        com = random.randint(0, 2)

        for i, desc in enumerate(hand):
            print(i, ":", desc)
        you = int(input("出す手を数値で入力:"))
        if you == 3: break
    except:
        print("0から3の間で入力してね")
        continue

    j = (int(hand[user_hand]) - int(hand[cpu_hand]) + 3) % 3
    if j == 0:
        print("あいこ")
    elif j == 1:
        print("負け(´;ω;｀)")
        count += 1
    else:
        print("勝ち(*'ω'*)")
        count += 1
        score += 1

# import random, print(), input(), if文, 比較演算子の練習