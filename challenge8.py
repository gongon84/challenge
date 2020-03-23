def Q(x):
    print("\n第",x,"問")

#1「正解」statisticsモジュール
if __name__ == "__main__":
    import statistics
    Q(1)
    list1 = [1,28,49,100]
    a = statistics.stdev(list1)
    print(a)


#2「正解」cubedモジュール使った関数
def cubed(x):
    return x ** 3
if __name__ == "__main__":
    print(cubed(3))
