from playsound import playsound
import os

print(os.listdir("soundbank"))
cwd = os.getcwd()
playsound(f"{cwd}/soundbank/C4vL.wav")