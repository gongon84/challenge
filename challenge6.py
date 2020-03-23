#1「正解」文字を１文字ずつ出力
print("\n第１問")
word = "カミュ"
print(word[0])
print(word[1])
print(word[2])


#2「正解」inputを用いて文章を完成させる
print("\n第2問")
word1 = input("何を書いた？：")
word2 = input("誰に送った？：")
a = "私は昨日 {}を書いて、{}に送った！".format(word1,word2)
print(a)


#3「正解」文字の先頭を大文字にする
print("\n第3問")
b = "aldous Huxley was born in 1894"
b = b.capitalize()
print(b)


#4「正解」文を分割してリストに
print("\n第4問")
c = "どこで？　誰が？　いつ？"
c = c.split( )
print(c)


#5「不正解」リストを1つの文字列に
print("\n第5問")
d = ["The","fox","jumped","over","the","fense","."]
d = " ".join(d)
#不正解部分
d = d[0:-2] + "."
print(d)


#6「正解」全てのsを¥に変える
print("\n第6問")
e = "A screaming comes across the sky."
e = e.replace("s","$s")
print(e)


#7「正解」最初にmが出現するインデックス
print("\n第7問")
f = "Hemingway"
f = f.index("m")
print(f)


#8「正解」クォーと文字が含まれてる文を文字列に
print("\n第8問")
g = "僕は\"肉\"を食べた"
print(g)


#9「正解」+と*を使って"three three three"という文字列
print("\n第9問")
h = "three" + " three" + " three"
i = "three " * 3
i = i.strip()
print(h)
print(i)


#「正解」10　スライスして"、"までの文字列
print("\n10問目")
j = "四月の晴れた寒い日で、時計がどれも十三時を打っていた。"
number = j.index("、")
#10を取得
print(number)
j = j[:10]
print(j)
