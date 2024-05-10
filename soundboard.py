import os
from pathlib import Path
root = Path(__file__).parent

def command():
    text = input("command: ").split()
    print(text)
    if len(text) == 0:
        command()
    if text[0]:
        if text[0] in ["help", "?"]:
            help()
        elif text[0] in ["exit", "quit", "q"]:
            exit()
        elif text[0] == "play":
            if len(text) == 2:
                play(str(text[1]))
            else:
                incorrect_usage("play")

def unknown():
    print("Unknown command")
    command()

def help():
    print("Commands:")
    print("help - show this message")
    print("exit - exit the program")
    print("play - play a sound")
    print("stop - stop playing a sound")
    command()

def intro():
    print("Welcome to the soundboard!")
    help()

def play(file):
    file = root/"files"/file
    os.startfile(file)
    command()


def incorrect_usage(user):
    print(f"Incorrect usage of {user}")
    if user == "play":
        print("Usage: play <sound>")
    command()



intro()