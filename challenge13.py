def Q(x):
    print("第",x,"問")

#1「正解」クラスを定義してメソッドをしよう
#2「正解」change_sizeメソッドを定義する
#3「不正解」shapeクラスを定義して継承させる
class Shape():
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return (self.width + self.height) * 2

class Square(Shape):
    def __init__(self,s):
        self.side = s

    def calculate_perimeter(self):
        return (self.side) * 4

    def change_size(self,x):
        self.side = self.side + x

Q(1)
rectangle1 = Rectangle(2,10)
square1 = Square(4)
print(rectangle1.calculate_perimeter())
print(square1.calculate_perimeter())

Q(2)
square1.change_size(10)
print(square1.side)

Q(3)
square1.what_am_i()
rectangle1.what_am_i()



#4「正解」Horse(馬)クラスとRider(騎手)クラスでコンポジションを使用
Q(4)

class Horse:
    def __init__(self,name,owner):
        self.name = name
        self.owner = owner

class Rider:
    def __init__(self,name,old):
        self.name = name
        self.old = old


juck = Rider("Juck x",20)
poti = Horse("Poti",juck)
print(poti.owner.name)
print(poti.owner.old)



    
