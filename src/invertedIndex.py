import json, sys

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

    # Open the input file for read and output file for write
    try:
        inputFile = open(arguments[1], 'r')
        outputFile = open(arguments[2], 'w')
    except IOError:
        error('Invalid file arguments')

    # Load and parse json data
    inputData = json.load(inputFile)
    # keys are the names of zones, and each value is a list of its values in all documents
    contents = {'doc_id' : []}
    for data in inputData:
        # Validate doc_id and it is unique
        try:
            ID = int(data['doc_id'])
        except ValueError:
            error('Invalid Document ID')
        if ID in contents['doc_id']:
            error('Invalid Repeated Document ID')

        # Save 
        for key in data.keys():
            if key in contents.keys():
                contents[key].append(data[key])
            else:
                contents[key] = [ data[key] ]

    print(contents)
    print('done')