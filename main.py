import os
import random


from playsound import playsound


notes = os.listdir("soundbank")
cwd = os.getcwd()
note = random.choice(notes)
print(f"Playing note {note}")
playsound(f"{cwd}/soundbank/{note}")


def main():
    pass

def play_sound(sounds, note):
    pass

def play_random_note(sounds):
    pass

def menu(desc, prompt, options):
    pass

def guess(guess, answer):
    return guess == answer
