#1「正解」歌手リスト
print("1問目")
singer = ["パソコン音楽クラブ","菊池桃子","森高千里"]
print(singer)


#2「プラスα」地名リスト、緯度経度タプル
print("\n２問目")
place = ["saitama","tokyo","okinawa"]
saitama = (35.52, 139.39)
tokyo = (36, 140)
okinawa = (26.1245, 127.4052)

print(place)
print("saitama:",saitama)
print("okinawa:",okinawa)


#3「正解」辞書　自分の特徴
print("\n3問目")
mine = {"name":"lussy", "height":"190", "体重":"りんご３個"}
print(mine)

#4「多分正解」任意のキーを用いて、上記のバリューを呼び出す
print("\n4問目")
number = input("""数字を入力してください:
    0: saitama
    1: tokyo
    2: okinawa
    number = """)
number = int(number)
if number < len(place):
    print(place[number])
else:
    print("他を入力してください")


#5「プラスα」辞書 (キー：歌手、バリュー：ソング)
print("\n5問目")
a = ["reiji no machi","inner blue"]
b = ["ガラスの草原","Adventure"]
c = ["１７才"]
singer_songs = {"パソコン音楽クラブ":a,"菊池桃子":b,"森高千里":c}
print(singer_songs)


#6 setとは？　listなどとの違い
print("\n6問目")
"""
listの重複をカウントしないバージョン
和集合や積集合などに使える
"""
list = [1,1,1,2,2,3,3,3,3]
set = {1,1,1,2,2,3,3,3,3}
print(list)
print(set)
