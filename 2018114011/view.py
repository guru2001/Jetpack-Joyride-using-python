from colorama import init
init()
from colorama import Fore,Style,Back
from board import *
from character import *
from random import randint as rd
import time

class coin1:
	def __init__(self):
		self.__coin = Fore.YELLOW  + Style.BRIGHT +  "$"  +   Style.RESET_ALL
		self.__coins = [[self.__coin],[self.__coin],[self.__coin],[self.__coin]]

	def retcoins(self):
		return self.__coin

	def setcoin(self,c):
		self.__coins = c

	def retcoin(self):
		return self.__coins

class coin2(coin1):	
	def __init__(self):
		coin1.__init__(self)
		self.setcoin([[self.retcoins(),self.retcoins(),self.retcoins(),self.retcoins(),self.retcoins(),self.retcoins()], [self.retcoins(),self.retcoins(),self.retcoins(),self.retcoins(),self.retcoins(),self.retcoins()]])

class coins(Board):
		def __init__(self,Board):
			
			self.__board = Board
		
		def place(self):
			coins = []
			cnt = 0
			a = 0
			
			while a < 1490:
				b = rd(3,41)
				a = a + rd(7,30)
				if a >= 1290 and a not in range(346,354) and a not in range(645,654) and a not in range(698,705) and a not in range(440,450) :
					break
				if rd(1,2) == 1:
					obj = coin1()
					coins.append(obj)
					cnt = cnt + 1
					for i in range(4):
						self.__board.ret_grid()[b + i][a] = coins[cnt - 1].retcoin()[i][0]
				else :
					obj = coin2()
					coins.append(obj)
					cnt = cnt + 1
					for i in range(2):
						for j in range(6):
							self.__board.ret_grid()[b + i][a + j] = coins[cnt - 1].retcoin()[i][j]


class beam1:
	def __init__(self):
		self.__beam_ends = Back.MAGENTA + "#" + Style.RESET_ALL
		self.__beam = Back.RED + "*" + Style.RESET_ALL
		self.__beam1 = [self.__beam_ends,self.__beam ,self.__beam ,self.__beam,self.__beam,self.__beam_ends]

	def ret_beam1(self):
		return self.__beam1

	def set_beam1(self,good):
		self.__beam1 = good
	
	def ret_beam_ends(self):
		return self.__beam_ends

	def ret_beam(self):
		return self.__beam
	def beam_disappear(self,mandalorian,Board):
		for i in range(mandalorian.retx() - 8,mandalorian.retx() + 8):
			for j in range(mandalorian.rety() - 8  , mandalorian.rety() + 8):
				if i > 0 and i < 44 and j > 0 and  j < Board.ret_presyp():
					if Board.ret_grid()[i][j] == self.ret_beam() or Board.ret_grid()[i][j] == self.ret_beam_ends() :
						Board.ret_grid()[i][j] = " "
	
	def beam_disappear1(self,mandalorian,Board):
		for i in range(mandalorian.ret__x()- 5 ,mandalorian.ret__x() + 5):
			for j in range(mandalorian.ret__y() - 5  , mandalorian.ret__y() + 10):
				if i > 0 and i < 44 and j > 0 and  j < Board.ret_presyp():	
					if Board.ret_grid()[i][j] == self.ret_beam() or Board.ret_grid()[i][j] == self.ret_beam_ends() :
						Board.ret_grid()[i][j] = " "
						mandalorian.set__activ(0)
						mandalorian.disappear(Board)
		if mandalorian.ret__activ() == 0:
			Board.set_score()


class beam3(beam1):
	def __init__(self):
		beam1.__init__(self)
		self.set_beam1([[self.ret_beam_ends()," "," "," "," "] ,[" ",self.ret_beam()," "," "," "], [" "," ",self.ret_beam()," "," "], [" "," "," ",self.ret_beam()," "], [" "," "," "," ",self.ret_beam_ends()]])

class beam2(beam1):
	def __init__(self):
		beam1.__init__(self)
		self.set_beam1([[self.ret_beam_ends()] ,[self.ret_beam()] ,[self.ret_beam()] ,[self.ret_beam()] ,[self.ret_beam_ends()]])

class beams(Board):
	def __init__(self,Board):
			self.__board = Board
		

	def place(self):
		a = 0
		b = 0

		while a < 1490:
			b = rd(4,41)
			a = a + rd(7,40)
			if a >= 1290 and a not in range(144,154) and a not in range(39,50) and a not in range(598,605) and a not in range(444,454) :
				break
			c = rd(1,3)
			cnt = 0
			beams = []
			if c == 1:
				dum = beam1()
				beams.append(dum)
				cnt = cnt + 1
				for i in range(6):
					self.__board.ret_grid()[b][a + i] = beams[cnt - 1].ret_beam1()[i]
			elif c == 2:
				dumm = beam1()
				dum = beam2()
				beams.append(dum)
				cnt = cnt + 1
				for j in range(5):
					self.__board.ret_grid()[b + j][a] = beams[cnt - 1].ret_beam1()[j][0]
			
			elif c == 3:
				dumm = beam1()
				dum = beam3()
				beams.append(dum)
				cnt = cnt + 1
				for i in range(5):
					for j in range(5):
						self.__board.ret_grid()[b + i][a + j] = beams[cnt - 1].ret_beam1()[i][j]

class Magnet(beam1):
	def __init__(self):
		beam1.__init__(self)
		self.__top = Fore.BLACK  + Style.BRIGHT + "_"  +Style.RESET_ALL
		self.__middle = Fore.BLUE + Style.BRIGHT +  "]"  + Style.RESET_ALL
		self.__bot = Fore.RED + Style.BRIGHT +  ":"  + Style.RESET_ALL
		self.set_beam1([[self.__top,self.__top,self.__top,self.__top,self.__top] ,[self.__middle," "," "," ",self.__middle] ,[self.__bot,self.__bot," ",self.__bot,self.__bot]])

class magnet(Board):
	def __init__(self,Board):
			self.__board = Board
			self.__y = 0

	def get_y(self):
		return self.__y

	def place(self):
		self.__y = rd(25,35)
		a1 = 150
		a2 = 450
		mag = []
		m1 = Magnet()
		m2 = Magnet()
		mag.append(m1)
		mag.append(m2)
		for i in range(3):
			for j in range(5):
				self.__board.ret_grid()[self.__y + i][a1 + j] = mag[0].ret_beam1()[i][j]
				self.__board.ret_grid()[self.__y + i][a2 + j] = mag[1].ret_beam1()[i][j]


class power_up(Board):
	def __init__(self,Board):
			self.__board = Board
			self.__top = Fore.WHITE  + Style.BRIGHT + "p"  +Style.RESET_ALL
	
	def ret_top(self):
		return self.__top




	def place(self):
		b = rd(25,35)
		a1 = 45
		a2 = 600
		mag = []
		m1 = power_up(self.__board)
		mag.append(self)
		mag.append(m1)
		for i in range(3):
			for j in range(5):
				self.__board.ret_grid()[b + i][a1 + j] = mag[0].__top
				self.__board.ret_grid()[b + i][a2 + j] = mag[1].__top



