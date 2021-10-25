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



    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.value = self.get_value()
        
    
    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other
        elif isinstance(other, str):
            return str(self) == other
        elif isinstance(other, Interval):
            return self.value == other.value
        return False

    def __str__(self):
        return str(self.value)


    def get_value(self):
        notes = ["a", "a#", "b", "c", "c#", "d", "d#", "e", "f", "f#", "g", "g#"]
        return abs(notes.index(self.start) - notes.index(self.end))

    def play(self):
        cwd = os.getcwd()
        playsound(f"{cwd}/octave4/{self.start}.mp3")
        playsound(f"{cwd}/octave4/{self.end}.mp3")
        return self

    def make_alternatives(self, notes, length=4):
        alts = [self]
        while len(alts) < length:
            temp = random.randint(0, 11)
            if temp not in alts:
                alts.append(temp)
        random.shuffle(alts)
        alt_dict = indexify(alts, letters=True)
        alt_dict["r"] = "Spela om"
        return alt_dict

    def sort(self, reverse = False):
        start = self.start
        end = self.end
        if (not reverse and start > end) or (reverse and start < end):
            self.start = end
            self.end = start
        




class Note:

    def __init__(self, value):
        self.value = value
    
    def __eq__(self, other):
        if isinstance(other, str):
            return self.value == other
        elif isinstance(other, Note):
            return self.value == other.value

        return False
    
    def __str__(self):
        return self.value
        
    def play(self):
        cwd = os.getcwd()
        playsound(f"{cwd}/octave4/{self.value}.mp3")
        return self

    def make_alternatives(self, notes, length=4):
        notes = notes.copy()
        notes.remove(self)
        alts = [self]
        for _ in range(length-1):
            temp = random_note(notes)
            notes.remove(temp)
            alts.append(temp)
        random.shuffle(alts)
        alt_dict =  indexify(alts)
        alt_dict["r"]  = "Spela om"
        return alt_dict

def splash():
    color_print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            Gehörsträning    
              
            Ett musikspel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""", bcolors.OKBLUE)

def main():
    splash()
    while True:
        choice = menu("Välj ett alternativ", "Val: ", {"p": "play", "q": "quit", "i": "intervall"})

        if choice in ("p", "play"):
            
            rounds = int(input("Antal omgångar: "))
            points = game(rounds)
            print(f"Du fick {points} poäng.\n")
        elif choice in ("i", "intervall"):
            rounds = int(input("Antal omgångar: "))
            points = game(rounds, intervall=True)
            print(f"Du fick {points} poäng.\n")
        else:
            break
    print("Hejdå!")
    #os.system('cls')

def game(rounds, intervall=False):
    points = 0
    notes = [e.strip(".mp3") for e in os.listdir("octave4")]
    notes.sort()
    

    for x in range(1, rounds+1):
        if intervall:
            correct = random_interval(notes)
        else:
            correct = random_note(notes)
        alternatives = correct.make_alternatives(notes)
        points += runda(x, rounds, notes, correct, alternatives)
    return points

def runda(current, end, notes, correct, alternatives):
    correct.play()
#    print(f"ANSWER: {correct}")

    answer = menu(f"({current}/{end})\nSvarsalternativ:", "Svar: ", alternatives)
    if guess(answer, correct, alternatives):
        color_print("Korrekt", bcolors.OKGREEN)
        return 1
    elif answer == "r":
        return runda(current, end, notes, correct, alternatives)
    else:
        color_print(f"Fel! Rätt svar var {correct}", bcolors.FAIL)
        return 0
    





def play_sound(notes, note):
    cwd = os.getcwd()
    playsound(f"{cwd}/octave4/{note}.mp3")
    return note

def random_note(notes):
    return Note(random.choice(notes))

def random_interval(notes):
    return Interval(random_note(notes), random_note(notes))

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

def indexify(lst, letters = False):
    if letters:
        return {f"{chr(i+97)}": e for i, e in enumerate(lst)}
    return {f"{i+1}": e for i, e in enumerate(lst)}


if __name__=="__main__":
    main()