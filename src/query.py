import sys

def error(name):
    '''
    Print out the error and exit the program with -1
    input: name is the name of the error
    '''
    print(name)
    exit(-1)

#Class Boolean
data_sues_lines = open("index.tsvline.tsv")

data_list = []

for line in data_sues_lines:
	if len(line) >1:
		data_list.append(line.split())

test_list = []

for i in data_list:
	if len(i) < 4:
		test_list.append(i)

for i in test_list:
	i[2] = int(i[2][1])

print(test_list)
print(len(test_list))
class Boolean:

	def __init__(self,data,query):

		self.data = data
		self.query = query
		self.binary_array = []


	# method retrieve
	def retrieve(self):
		for i in self.data:
			self.binary_array.append(0)
		return self.binary_array
		


	# method AND


	# method OR


'''
if __name__ == "__main__":
    # Get the arguments and validate the number
    arguments = sys.argv
    if len(arguments) != 3:
        error("Invalid arguents")

    print('done')
'''
query = "test"
boolean = Boolean(test_list,query)
result = boolean.retrieve()
print(result)