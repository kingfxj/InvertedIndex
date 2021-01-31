import boolean, sys

def error(name):
    print(name)
    exit(-1)

if __name__ == "__main__":
    arguments = sys.argv
    if len(arguments) != 3:
        error("Invalid arguents")