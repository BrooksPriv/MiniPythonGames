import random

def CodeGuess():
    h = 0
    g = 0
    x = ""
    guess = []
    colors = ["R", "G", "B", "Y"]
    code_length = 4
    secret_code = random.choices(colors, k=code_length) 
    
    while guess != secret_code:
        while len(x) != 4:
            x = input("guess 4 colors by their first letter: ").upper()
            if x == "STOP":
                return "Stop"
        guess = list(x)
        if len(guess) == 4 and guess != secret_code:
            print("try again")
            guess = []
            
        if g%4 ==0:
            print(f"Hint: {secret_code[h]}")
            h+=1
            
        x = ""
        g +=1
            
    print("correct")

CodeGuess()
