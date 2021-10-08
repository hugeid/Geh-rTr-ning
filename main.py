import os
import sys
import random


from playsound import playsound


notes = os.listdir("soundbank")
cwd = os.getcwd()
note = random.choice(notes)
#print(f"Playing note {note}")


def splash():
    print("""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              Biathlon
              
         a hit or miss game
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")

def main():
    while True:
        if menu("Välj ett alternativ", "Val: ", {"p": "play", "q": "quit"}) == "p":
            notes = os.listdir("soundbank")
            correct = random_note(notes) 
            alternatives = make_alternatives(notes, correct)
            runda(notes, correct, alternatives)
        else:
            break
    print("Hejdå!")
    #os.system('cls')


def runda(notes, correct, alternatives):
    play_sound(notes, correct)
    print(f"\nCorrect: {correct}\n")

    answer = menu("Välj ett alternativ", "Val: ", alternatives)
    if guess(alternatives[answer], correct):
        print("Korrekt!")
    elif answer == "r":
        runda(notes, correct, alternatives)
    else:
        print(f"\nFel! Rätt svar var {correct}")

def make_alternatives(notes, correct, length=4):
    temp = str(random.randint(1, length))
    temp_dict = {}
    for x in range(1, length+1):
        if str(x) != temp:
            note = random_note(notes)
            while note in temp_dict:
                note = random_note(notes)
            temp_dict[str(x)] = random_note(notes)
        else:
            temp_dict[temp] = correct
    temp_dict["r"] = "Spela om"
    return temp_dict


def play_sound(notes, note):
    cwd = os.getcwd()
    playsound(f"{cwd}/soundbank/{note}")
    return note

def random_note(notes):
    return random.choice(notes)

def menu(desc, prompt, options):
    print(f"{desc}\n")
    for key, value in options.items():
        print(f"{key}. {value}")
    while True:
        a = input(prompt)
        if a in options:
            return a


def guess(guess, correct):
    return guess == correct

if __name__=="__main__":
    main()