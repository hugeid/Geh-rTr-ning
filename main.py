import os
import sys
import random


from playsound import playsound



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

def splash():
    color_print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            Gehörsträning    
              
            Ett musikspel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""", bcolors.OKBLUE)

def main():
    splash()
    while True:
        svar = menu("Välj ett alternativ", "Val: ", {"p": "play", "q": "quit", "i": "intervall"})
        if svar  in ("p", "play"):
            rounds = int(input("Antal omgångar: "))
            points = game(rounds)
            print(f"Du fick {points} poäng.\n")
        elif svar in ("i", "intervall"):
            pass
        else:
            break
    print("Hejdå!")
    #os.system('cls')

def game(rounds):
    points = 0
    notes = [x.strip(".mp3") for x in os.listdir("octave4")]

    for _ in range(1, rounds+1):
        correct = random_note(notes) 
        alternatives = make_alternatives(notes, correct)
        points += runda(x, rounds, notes, correct, alternatives)
    return points

def runda(current, end, notes, correct, alternatives):
    play_sound(notes, correct)
    print(f"ANSWER: {correct}")

    answer = menu(f"({current}/{end})\nSvarsalternativ:", "Svar: ", alternatives)
    if guess(answer, correct, alternatives):
        color_print("Korrekt", bcolors.OKGREEN)
        return 1
    elif answer == "r":
        return runda(current, end, notes, correct, alternatives)
    else:
        color_print(f"Fel! Rätt svar var {correct}", bcolors.FAIL)
        return 0
    

def make_alternatives(notes, correct, length=4):
    notes = notes.copy()
    notes.remove(correct)
    alts = [correct]
    for _ in range(length-1):
        temp = random_note(notes)
        notes.remove(temp)
        alts.append(temp)
    random.shuffle(alts)
    alt_dict =  indexify(alts)
    alt_dict["r"]  = "Spela om"
    return alt_dict

def play_sound(notes, note):
    cwd = os.getcwd()
    playsound(f"{cwd}/octave4/{note}.mp3")
    return note

def random_note(notes):
    return random.choice(notes)

def menu(desc, prompt, options):
    print(f"{desc}\n")
    for key, value in options.items():
        print(f"    {key}) {value}")
    print()
    while True:
        a = input(prompt)
        if a in options or a in options.values():
            return a
    

def guess(guess, correct, alternatives):

    return guess == correct or (guess in alternatives and alternatives[guess] == correct)

def color_print(text, color):
    print(f"\n{color}{text}{bcolors.ENDC}")

def indexify(lst):
    return {f"{i+1}": e for i, e in enumerate(lst)}

if __name__=="__main__":
    main()