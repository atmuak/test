print('数字３桁のパスワードを設定してください')

pass_list = list()

user_pass = int(input("パスワードを数値で入力:"))

for clear in range(0, 1000, 1):
    print ('{:0=3}'.format(clear))
    if clear == user_pass:
        print('解除！')
        break

print('あなたが設定したパスワードは' + str(clear) + 'です')