from colorama import init, Fore, Style
from collections import Counter
from english_words import get_english_words_set
import random

def Wordle(Word, l):
    init()
    WordA = list(Word.lower())


    for z in range(1,6):
        #Var
        Inp = ""
        z = ""
        t = []

        print(l)

        #Ask the player
        while(len(Inp) != 5):
            Inp = input(f"{Fore.BLACK}Enter a 5 letter word: ")
            if len(Inp) !=5 and Inp not in l:
                print("Try Again (Hint has to be 5 letters)")

        #Duplicates
        counts = Counter(Inp)
        countsWord = Counter(Word)
        duplicates = [char for char, count in counts.items() if count > 1]
        for x in WordA:
           # print(x)
            if x in countsWord == 1:
                del countsWord[x]

        #Makes Input of player into a list
        Inp = list(Inp.lower())

        #Win
        if Inp == WordA:
            z = "".join(Inp)
            return (f"{Fore.GREEN} {z}!!").replace(" ", "")

        #Check for right Place
        for x in range(len(WordA)):
            if WordA[x] == Inp[x]:
                z = (f"{z}{Fore.GREEN} {Word[x]}")
            elif Inp[x] in WordA:
                if duplicates == ([char for char, count in (Counter(WordA)).items() if count >1]):
                    z = f"{z}{Fore.YELLOW}{Inp[x]}"
                elif list(Inp[x]) != duplicates:
                    z = f"{z}{Fore.YELLOW}{Inp[x]}"
                else:
                    z = f"{z}{Fore.BLACK}{Inp[x]}"
            elif WordA[x] != Inp[x]:
                z = f"{z}{Fore.BLACK}{Inp[x]}"
        print(z.replace(" ", ""))
    print(f"{Fore.GREEN} {Word}")

word_set = get_english_words_set(['web2'], lower=True)
five_letter_words = [word for word in word_set if len(word) == 5]
random_word = random.choice(five_letter_words)

print(Wordle(random_word,word_set))
