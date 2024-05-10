import os
from pathlib import Path

root = Path(__file__).parent
destination = root/"files"

def command():
    text = input("command: ").split(" ", 1)
    if len(text) == 0 or text[0] in {"", " "} or text[0] is None:
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
        elif text[0] in ["list", "ls"]:
            givelist()
        elif text[0] in ["remove", "delete", "rm"]:
            if len(text) == 2:
                remove(text[1])
            else:
                incorrect_usage("remove")
        else:
            unknown()
def unknown():
    print("Unknown command")
    command()

def help():
    print("--------------------")
    print("Commands:")
    print("help - show this message")
    print("exit - exit the program")
    print("play - play a sound")
    print("upload - upload a sound")
    print("list - list available sounds")
    print("remove - remove a sound")
    
    print("--------------------")
    command()

def play(file):
    filename = str(file).rsplit(".",1)[0]
    if not os.path.exists(destination):
        os.mkdir(destination)
    file = destination/file
    print("--------------------")
    print(f"Playing {filename}")
    print("--------------------")
    try: os.startfile(file)
    except: print(f"Could not play {filename}")
    print("--------------------")
    command()

def upload(file):
    print("--------------------")
    print(f"Uploading {file}")
    print("--------------------")
    if not os.path.exists(destination):
        os.mkdir(destination)
    try: os.system(f"copy {file} {destination}")
    except: print(f"Could not upload {file}, please make sure the path is absolute")
    print("--------------------")
    command()

def givelist():
    print("--------------------")
    print("Available sounds:")
    files = set()
    if not os.path.exists(root/"files"):
        os.mkdir(root/"files")
    for file in os.listdir(destination):
        filename = str(file).rsplit(".",1)[0]
        files.add(filename)
    files_str="  |  ".join(files or ["No sounds available"])
    print(files_str)
    print("--------------------")
    command()

def remove(file):
    file = f"{file}.mp3"
    print("--------------------")
    print(f"Removing {file}")
    print("--------------------")
    try: os.remove(destination/file)
    except: print(f"Could not remove {file}")
    command()

def incorrect_usage(passed_command):
    print("--------------------")
    print(f"Incorrect usage of {passed_command}")
    if passed_command == "play":
        print("Usage: play <sound>")
    elif passed_command == "upload":
        print("Usage: upload <path>")
    elif passed_command == "remove":
        print("Usage: remove <sound>")
    print("--------------------")
    command()
    
    
def intro():
    print("Welcome to the soundboard!")
    help()
    
intro()