import time
class Shield:
	def __init__(self):
		self.__prev = 0
		self.__act1 = 0
		self.__act = 0

	
	def ret_prev(self):
		return self.__prev

	def retact(self):
		return self.__act
	
	def setact(self,x):
		self.__act = x
	
	def setact1(self,x):
		self.__act1 = x

	def set_prev(self,x):
		self.__prev = x

	def check(self,mandalorian,Board):
		if mandalorian.ret_add(Board) - self.__prev >= 60 or self.__prev == 0:
			self.setact1(1)
			self.activate(mandalorian,Board)
		else:
			self.setact1(0)
	
	def check1(self,mandalorian,Board):
		if mandalorian.ret_add(Board) - self.__prev <= 10 and self.__prev != 0 :
			self.setact(1)
		else:
			self.setact(0)


	def activate(self,mandalorian,Board):
		if self.__act1 == 1 and self.__act == 0:
			self.setact(1)
			self.set_prev(mandalorian.ret_add(Board))
