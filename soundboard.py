import os
from pathlib import Path
root = Path(__file__).parent

def command():
    text = input("command: ").split(" ", 1)
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
                play(text[1])
            else:
                incorrect_usage("play")
        elif text[0] == "upload":
            if len(text) == 2:
                upload(text[1])
            else:
                incorrect_usage("upload")

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
    filename = str(file).rsplit(".",1)[0]
    print(f"Playing {filename}")
    file = root/"files"/file
    os.startfile(file)
    command()

def upload(file):
    print("Uploading a sound")
    destination = root/"files"
    os.system(f"copy {file} {destination}")
    command()


def incorrect_usage(passed_command):
    print(f"Incorrect usage of {passed_command}")
    if passed_command == "play":
        print("Usage: play <sound>")
    elif passed_command == "upload":
        print("Usage: upload <sound>")
    command()


intro()