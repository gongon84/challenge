#第n問の定義
def Q(n):
    print("\n第",n,"問")

#1「正解」リストの要素を出力
Q(1)
a = ["ウォーキング・デッド","アントラージュ","ザ・ソプラノズ","ヴァンパイア・ダイアリーズ"]
for show in a:
    print(show)


#2「正解」２５〜５０まで出力
Q(2)
for i in range (25,51):
    print(i)


#3「正解だけど不正解」Q1をインデックス値と一緒に
Q(3)
for index, show in enumerate(a):
    print(index,show)
    
"""
最初の回答
n = 0
for show in a:
    print(n,":",show)
    n += 1
"""


#4「正解」無限ループする数字当て
Q(4)
b = [2,13,27,100]
while True:
    c = input("数字を入力してください：")
    if c == "q":
        break
    else:
        try:
            c = int(c)
            if c in b:
                print("正解")
                break
            else:
                print("不正解")
        except:
            print("数字を入力するか、qで終了します")


#5「正解」二つのリストの数字を掛け算
Q(5)
d = [8, 19, 148, 4]
e = [9, 1, 33, 83]
f = []
for i in d:
    for j in e:
        f.append(i * j)
print(f)
