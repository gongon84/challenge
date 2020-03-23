def print_string(string):
    print(string)

print_string("Testing: 1, 2, 3.")





#1
def squared(x):
    """
    Return x**2.
    :Param x: float.
    :return: square of x.
    """
    return x ** 2

x = input("[1]type a number:")
x = float(x)
print("x ** 2 =",squared(x))


#2
def st(x):
    return str(x)

y = input("[2]文字を入力してください:")
print("入力した文字は",st(y))


#3
def five(a,b,x=1,y=2,z=3):
    return x + y + z + a + b
a = input("[3]数字を入力してください")
a = int(a)
b = input("[3]数字を入力してください")
b = int(b)
print("a + b + 6 =",five(a,b))


#4
def su(x):
    return x / 2

def suu(x):
    return x * 4

z = input("[4]整数を入力してください:")
z = float(z)
print("z / 2 =",su(z))
c = float(su(z))
print("c * 4 =",suu(c))


#5
d = input("[5]文字を入力してください:")
d = str(d)
try:
    print(float(d))
except (ValueError):
    print("これは入力できません")
