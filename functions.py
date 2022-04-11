
# 1番目に入力した数字を二番目に入力した数字で割り、
# 得られた値が整数である場合にその値を表示する関数です



def calc(x,y):
    a = x / y
    int(a)
    if a.is_integer():
        print(a)
    else:
         print("入力した数字は割り切れません")




# Xの入力（文字と負の入力を除外）

X = input("A. 1番目の入力: 0より大きい値を入力してください: ")
while X.isdigit == False:
        X = input("A. 1番目の入力: 0より大きい値を入力してください: ")    
# intに変換
input_x = int(X)

while input_x < 0:
        X = input("B. 1番目の入力: 0より大きい値を入力してください: ")    
print(X,"と入力されました")
print("次の入力です")

# yの入力（文字と負の入力を除外）
Y = input("A. 2番目の入力: 0より大きい値を入力してください: ")
while Y.isdigit == False:
        Y = input("A. 2番目の入力: 0より大きい値を入力してください: ")    

# intに変換
input_y = int(Y)
while input_y < 0:
        Y = input("B. 2番目の入力: 0より大きい値を入力してください: ")    
print(Y,"と入力されました")
print("計算します...")


calc(input_x,input_y)