def Q(x):
    print("第",x,"問")

#1「正解」クラス変数を作り、オブジェクトをリストに入れる
#2「不正解」print関数で４辺を表示
Q(1)

class Square():
    square_list = []

    def __init__(self,side):
        self.side = side
        self.square_list.append(self.side)

    def __repr__(self):
        return ("{} by {} by {} by {}" \
                  .format(self.side,self.side,self.side,self.side))


a = Square(3)
b = Square(8)
c = Square(102)
print(Square.square_list)

Q(2)
print(a)


#3「不正解」同じオブジェクトを渡されたらTrue、違かったらFalseの関数
Q(3)

def compare(obj1,obj2):
    return obj1 is obj2

print(compare("a","a"))
