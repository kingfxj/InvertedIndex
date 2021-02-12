test_list_2 = [['1',1,[0]],
['2',2,[0,1]],
['three',1,[4]],
['four',6,[1,3,5,6,7,8]],
['five',3,[1,2,3]],
['six',2,[0,6]],
['seven',4,[1,5,8,9]],
['eight',1,[3]]]
tes_q = ["four AND five","1 OR six", "seven AND NOT eight","four OR (2 AND seven)"]
tes_q = ["four AND five"]

class Posting:
	def __init__(self,data,target):
		self.target = target
		self.data = data
		self.word = ''
		self.ids = ''

	def lookUp(self):
		for index in self.data:
			if index[0] ==self.target:
				self.word = index[0]
				self.ids = index[2]

		

	def getPosting(self):
		return [self.word,self.ids]

class Boolean:

	def __init__(self,posting_1,posting_2):
		self.posting_1 = posting_1
		self.posting_2 = posting_2
		self.p1_length = len(posting_1[1]) 
		self.p2_length = len(posting_2[1]) 


	def getAnd(self):
		pointer_1 = 0
		pointer_2 = 0
		answer = []
		while pointer_1!= self.p1_length and pointer_2 != self.p2_length:
			if self.posting_1[1][pointer_1] ==self.posting_2[1][pointer_2]:
				answer.append(self.posting_1[1][pointer_1])
				pointer_1 +=1
				pointer_2 +=1
			elif self.posting_1[1][pointer_1] <self.posting_2[1][pointer_2]:
				pointer_1 +=1
			else:
				pointer_2 +=1
		return answer


	def getOr(self):
		pass

	def getAndNot(self):
		pass


posting_1 = Posting(test_list_2,'four')
posting_2 = Posting(test_list_2,'seven')
posting_1.lookUp()
posting_2.lookUp()

posting_1 = posting_1.getPosting()
posting_2 = posting_2.getPosting()

boolean = Boolean(posting_1,posting_2)

boolean.getAnd()
print(boolean.getAnd())