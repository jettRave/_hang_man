'''
Created on May 19, 2021

@author: michael
'''
import os
from random import randint
import sys

run_p = True

while run_p == True:
    run_p = False
    body = [" ", " ", " ", " ", " ", " "]
    dead = ["o", "|", "/", "\\", "/", "\\"]
    in_put = ""
    file = open(__file__.replace("_hang_man.py", "") +
                "_hang_man_words.txt", "r")
    file_list = file.readlines()
    file.close()
    count = 0
    s_word = file_list[randint(0, len(file_list))].upper().rstrip()
    word = s_word

    def clear():
        os.system("clear")

    def draw_body(in_put):
        clear()
        print("  ______\n  |    |\n  " + body[0] + "    |\n " + body[2]
              + body[1] + body[3] + "   |\n " + body[4] + " " + body[5]
              + "   |\n ______|\n" + word + "\n" + in_put)

    def typed_letters(guess, in_put):
        if in_put.find(guess) == -1:
            return in_put + guess
        else:
            return in_put

    for i in word:
        word = word.replace(word[word.find(i)], "-")

    while count < 6 and word != s_word:
        draw_body(in_put)
        guess = input("Enter a Letter: ")
        guess = guess.upper()
        if guess == "EXIT":
            count = 7
        elif len(guess) != 1 or not guess.isalpha():
            input("ERROR NOT A LETTER")
        elif in_put.find(guess) != -1:
            input("Letter Already Used")
        elif s_word.find(guess) != -1:
            i = -1
            lword = []
            in_put = typed_letters(guess, in_put)

            for x in word:
                lword.append(x)

            while s_word.find(guess, i + 1, len(s_word)) != -1:
                lword[s_word.find(guess, i + 1, len(s_word))] = guess
                i += 1
            word = ""
            for x in lword:
                word = word + x
        else:
            in_put = typed_letters(guess, in_put)
            body[count] = dead[count]
            count += 1
    draw_body(in_put)
    print(s_word)

    if count > 6:
        clear()
    else:
        if count >= 6:
            print("You Lose")
        elif word == s_word:
            print("You Win")
        end = input("Type R to reset: ").upper()
        if end == "R":
            run_p = True
        clear()
