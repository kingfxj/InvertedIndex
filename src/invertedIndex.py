import json, sys

def error(name):
    print(name)
    exit(-1)

if __name__ == "__main__":
    arguments = sys.argv
    if len(arguments) != 3:
        error("Invalid arguents")
    try:
        inputFile = open(arguments[1], 'r')
        outputFile = open(arguments[2], 'w')
    except IOError:
        error('Invalid file arguments')

    inputData = json.load(inputFile)
    docId = []
    for data in inputData:
        try:
            ID = int(data['doc_id'])
        except ValueError:
            error('Invalid Document ID')
        if ID in docId:
            error('Invalid Document ID')
        docId.append(ID)
    print('done')