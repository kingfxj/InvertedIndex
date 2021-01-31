import boolean, sys

def error(name):
    '''
    Print out the error and exit the program with -1
    input: name is the name of the error
    '''
    print(name)
    exit(-1)

if __name__ == "__main__":
    # Get the arguments and validate the number
    arguments = sys.argv
    if len(arguments) != 3:
        error("Invalid arguents")

    print('done')