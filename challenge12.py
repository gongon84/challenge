import math

def Q(x):
    print("\n第",x,"問")


#1「正解」4つの属性をインスタンス変数に持つ、apple属性を定義
Q(1)

class Apple:
    def __init__(self,w,c,s,p):
        #重さ(w)、色(c)、サイズ(s)、値段(p)
        self.weight = w
        self.color = c
        self.size = s
        self.price = p
        print("作成しました")


#2「正解」円を表すcircleクラスを定義
Q(2)
class Circle:
    def __init__(self,r):
        #半径(r)
        self.radius = r
        print("円を作成しました。 半径：",r)

    def area(self):
        return (self.radius ** 2) * math.pi

circle1 = Circle(4)
area1 = circle1.area()
print("面積：",area1)


#3「正解」三角形を表すTriangleクラスを定義
Q(3)
class Triangle:
    def __init__(self,us,s2,s3,h):
        #底辺(us)、他の２辺(s2,s3)、高さ(h)
        self.underside = us
        self.side2 = s2
        self.side3 = s3
        self.hight = h
        print("三角形を作成しました")

    def area(self):
        return (self.underside * self.hight) / 2

    def area_2(self):
        x = (self.underside + self.side2 + self.side3) / 2
        return math.sqrt( \
            x * (x - self.underside) * (x - self.side2) * (x - self.side3) \
            )

triangle1 = Triangle(3,"unknown","unknown",100)
triangle2 = Triangle(3,4,5,"unknown")
area1 = triangle1.area()
area2 = triangle2.area_2()
print(area1)
print(area2)


#4「正解」六角形を表すHexagonクラスを定義
Q(4)

class Hexagon:
    def __init__(self,s1,s2,s3,s4,s5,s6):
        #各辺１〜６
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
        self.side4 = s4
        self.side5 = s5
        self.side6 = s6
        print("六角形を作成しました")

    def culculate_perimeter(self):
        sum = self.side1 + self.side2 + self.side3 + \
              self.side4 + self.side5 + self.side6
        return sum

hexagon1 = Hexagon(2,3,5,1,5,3)
perimeter1 = hexagon1.culculate_perimeter()
print(perimeter1)



    


