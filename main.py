import os
import random


from playsound import playsound


notes = os.listdir("soundbank")
cwd = os.getcwd()
note = random.choice(notes)
print(f"Playing note {note}")
playsound(f"{cwd}/soundbank/{note}")

