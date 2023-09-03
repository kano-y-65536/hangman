def hangman(word):
    wrong = 0
    stages = ["",
             "_____     ",
             "|    |    ",
             "|    o    ",
             "|   /|\   ",
             "|   / \   ",
             "|         ",
             "|         "
             ]
    rletters = list(word)
    board = ["_"]*len(word)
    win = False
    print("Welcome to hangman!")
    
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Predict a character in the word."
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("\n")
            print("You win!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n")
        print("You lose!")
        print("The word is {}.".format(word))


num = int(input("How many characters should the word be?"))
wordlist2 = []
import random
import pathlib
p =pathlib.Path( "p.139_hangman_wordlist.txt")

with open(p.resolve(),"r",encoding="utf-8") as f:
    wordlist1 = f.readlines()
    for word_in_list1 in wordlist1:
        if len(word_in_list1) <= num + 1:
            wordlist2.append(word_in_list1)

r = random.randint(1,len(wordlist2))
selected = wordlist2[r]
num_selected = len(selected)
w = selected[0:num_selected-1]

hangman(w)
