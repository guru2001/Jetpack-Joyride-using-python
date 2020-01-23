from character import *
from board import *
from colorama import Style,Fore,Back,init
from view import *
init()
import time


class Power:
	def __init__(self):
		self.__prev = 0
		self.__act = 0
		self.__top = Fore.WHITE  + Style.BRIGHT + "p" + Style.RESET_ALL

	def ret_top(self):
		return self.__top

	def ret_prev(self):
		return self.__prev


	def setact(self,x):
		self.__act = x

	def retact(self):
		return self.__act

	def set_prev(self,x):
		self.__prev = x

	
	def check1(self,mandalorian,Board):
		if mandalorian.ret_add(Board) - self.__prev <= 6 and self.__prev != 0 :
			self.setact(1)
		else:
			self.setact(0)


	def activate(self,mandalorian,Board):
			self.setact(1)
			self.set_prev(mandalorian.ret_add(Board))

	def Power_disappear(self,Board,mandalorian):
		for i in range(mandalorian.retx() - 15,mandalorian.retx() + 15):
			for j in range(mandalorian.rety() - 15  , mandalorian.rety() + 15):
				if i > 0 and i < 44 and j > 0 and  j < Board.ret_presyp():
					if Board.ret_grid()[i][j] == self.__top:
						Board.ret_grid()[i][j] = " "
	
	def Power_fn(self,Board,mandalorian):
		for i in range(mandalorian.retx() - 3,mandalorian.retx() + 3):
			for j in range(mandalorian.rety() - 4, mandalorian.rety() + 4):
				if Board.ret_grid()[i][j] == self.__top:
					Board.ret_grid()[i][j] = " "
					self.Power_disappear(Board,mandalorian)
					self.activate(mandalorian,Board)
