import re

def Q(x):
    print("第",x,"問")

#1「ちょい正解」正規表現、booやloo
Q(3)
line = "The ghost that says boo haunts the loo"
found = re.findall(".oo",line)
print(found)

