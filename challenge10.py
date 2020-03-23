#1「」単語をリストからランダムに
import random

def hangman(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        char = input("単語を推測してください：")
        if char in rletters:
            cind = rletters \
                   .index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        word1 = (" ".join(board))
        print("ワード：",word1)
        e = wrong + 1
        print("\n".join(stages[0: e]))
        x = (len(stages) - 1) - wrong
        if x == 0:
            break
        else:
            print("\nあと",x,"回で負けです")
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("You lose! It was {}."
              .format(word))

list1 = ["cat","dog","pig","fox","bat"]
hangman(random.choice(list1))

