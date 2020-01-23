from person import Person
from board import Board
import time
from collection import collection_coins
from colorama import Fore,Back,init,Style
from view import *
from affect import *
from collection import *
init()

class mandalorian(Person):

	def __init__(self):
		Person.__init__(self)
	
		self.__matrix = [[" ",".","."," "],["["," "," ","]"],[" ","|","|"," "]]
		self.__matrix_wc = [[" ",".","."," "],["["," "," ","]"],[" ","|","|"," "]]
		self.__upmatrix = [[" ",".","."," "],["["," "," ","]"],[" ","N","N"," "]]
		self.__shield = [[" ",".",".","#"],["["," "," ","]"],[" ","|","|","#"]]
		self.__upshield = [[" ",".",".","#"],["["," "," ","]"],[" ","N","N","#"]]
		self.__add = 0
		self.__bshape = Fore.GREEN + Style.BRIGHT + Back.RED + "o" +Style.RESET_ALL
		self.__bx = self.retx() + 1
		self.__by = self.rety() + 1
		self.__bactiv = 0
		
	def ret__activ(self):
		return self.__bactiv
	def set__activ(self,x):
		self.__bactiv = x
	def update_bx(self):
		self.__bx = self.retx() + 1
	def update_by(self):
		self.__by = self.rety() + 1

	def ret__x(self):
		return self.__bx
	
	def ret__y(self):
		return self.__by

	def set__y(self,x):
		self.__by = x

	def disappear(self,Board):
		if self.ret__y() < 1490: 
			Board.ret_grid()[self.ret__x()][self.ret__y()] = " "

	def upgrade(self,Board,b):
		if self.ret__y() + 10 >= Board.ret_presyp():
			self.disappear(Board)
			self.__bactiv = 0
			a = beam1()
	
		else:
			self.set__y(self.ret__y() + 10)
			# self.check(Board,a,b)


	def check(self,Board,beam1,b):
		touch_beam3(Board,self,beam1)
		b.Boss_life(Board,self)

	def appear(self,Board,b):
		if self.ret__y() + 20 <= 1499:
			Board.ret_grid()[self.ret__x()][self.ret__y()] = self.__bshape
			self.__bactiv = 1
			a = beam1()

			self.check(Board,a,b)

	def ret_upshield(self):
		self.__matrix = self.__upshield


	def ret_add(self,Board):
		return time.time() - Board.ret_stime()
	
	def update_mand(self,Board,sh2,sh,dum,dum2):
		self.delete_mand(Board)
		if sh2 == 1:
			if self._y + 3 <= 1310 :
				self.__add = int((time.time() - Board.ret_stime()))
				self.sety(self.rety() + 3)
				if self.rety() < Board.ret_presy():
					self.sety(Board.ret_presy())
				collection_coins(Board,self,dum)
				touch_beam(Board,self,dum2,sh)	
				self.paste_mand(Board)
				Board.printit(sh2,self)
			elif self._y + 3 > 1310 :
				collection_coins(Board,self,dum)
				touch_beam(Board,self,dum2,sh)
				self.paste_mand(Board)
				Board.printit2(sh2,self)
		else:
			if self.rety() + 1 <= 1310 :
				self.__add = int((time.time() - Board.ret_stime()))
				self.sety(self.rety() + 1)
				if self.rety() < Board.ret_presy():
					self.sety(Board.ret_presy())
				collection_coins(Board,self,dum)
				touch_beam(Board,self,dum2,sh)
				self.paste_mand(Board)
				Board.printit(sh2,self)
			elif self.rety() + 1 > 1310:
				collection_coins(Board,self,dum)
				touch_beam(Board,self,dum2,sh)
				self.paste_mand(Board)
				Board.printit2(sh2,self)	


	def paste_mand(self,Board):
			for i in range(self._x,self._x + 3):
				for j in range(self._y  , self._y  + 4):
					Board.ret_grid()[i][j] = self.__matrix[i - self._x][j - self._y]
		 

	def delete_mand(self,Board):
			for i in range(self._x,self._x + 3):
				for j in range(self._y  , self._y + 4):
					Board.ret_grid()[i][j] = " "
				
	def set_upmatrix(self):
		self.__matrix = self.__upmatrix


	def same_matrix(self):
		self.__matrix = self.__matrix_wc			

	def shield(self):
		self.__matrix = self.__shield

class boss_create(Person):
	def __init__(self):
		Person.__init__(self)
		self._x = 34
		self._y = 1440
		self.__iceball = Fore.CYAN + Back.WHITE + Style.BRIGHT + "@" + Style.RESET_ALL
		self.__shape = []
		self.__bx = self._x - 2
		self.__by = self._y - 2
		self.__act = 0
		self.__time = time.time()
		self.__lives = 5
		with open("boss.txt") as obj:
			for line in obj:
				self.__shape.append(line.strip('\n'))

	def boss_update(self,Board):
		if self._x >= 12 and self._x <= 34:
			for i in range(self._x  ,self._x + 9):
				for j in range(self._y,self._y + 9):
					if i <= 43 and j < 1500:
						Board.ret_grid()[i][j] = self.__shape[self._x - i][self._y - j]

	
	def boss_ac_disappear(self,Board):
		for i in range(self._x  ,self._x + 9):
			for j in range(self._y,self._y + 9):
				if i <= 43 and j < 1500:
					Board.ret_grid()[i][j] = " "

	def boss_movement(self,Board,mandalorian,sh):
		self.boss_ac_disappear(Board)

		if mandalorian._x <= 39 and  mandalorian._x >= 8:			
			self._x = mandalorian._x - 5
		elif mandalorian._x >= 39:
			self._x = 34
		elif mandalorian._x <= 8:
			self._x = 3

		for i in range(self._x  ,self._x + 9):
			for j in range(self._y,self._y + 9):
				if i <= 43 and j < 1500:
					Board.ret_grid()[i][j] = self.__shape[self._x - i][self._y - j]

		if self.returnact() == 1:
			self.Boss_bullets_movement(mandalorian,Board,sh)
		else:
			self.Boss_bullets(mandalorian,Board,sh)



	def retbx(self):
		return self.__bx
	def retby(self):
		return self.__by
	def setby(self,x):
		self.__by = x
	def setbx(self,x):
		self.__bx = x
	def timeset(self,x):
		self.__time = x
	def timeret(self):
		return self.__time
	def returnact(self):
		return self.__act
	def setact(self,x):
		self.__act = x
	def retice(self):
		return self.__iceball
	def retlives(self):
		return self.__lives
	def setlives(self,x):
		self.__lives = x

	def Boss_bullets(self,mandalorian,board,sh):
		if int(time.time() - self.timeret()) >= 5:
			self.timeset(time.time())
			self.setbx(self.retx())
			self.setby(self.rety())
			board.ret_grid()[self.retbx()][self.retby()] = self.retice()
			self.Boss_bullets_movement(mandalorian,board,sh)
			self.setact(1)
		
	
			
	def Boss_disappear(self,board):
		board.ret_grid()[self.retbx()][self.retby()] = " "


	def Boss_bullets_movement(self,mandalorian,board,sh):
		self.Boss_disappear(board)
		self.setby(self.retby() - 8)
		if self.retby() >= 1290 :
			board.ret_grid()[self.retbx()][self.retby()] = self.retice()
			self.check_collision(mandalorian,board,sh)
		else:
			self.setact(0)

	def check_collision(self,mandalorian,board,sh):
 		for i in range(mandalorian.retx(),mandalorian.retx() + 3):
 			for j in range(mandalorian.rety()  , mandalorian.rety()  + 4):
 				if i == self.retbx() and j == self.retby():
 					if sh == 0:
 						board.set_lives()
 					# board.set_lives()
 					self.Boss_disappear(board)
 					self.setact(0)
 					return
 			


	def Boss_life(self,Board,mandalorian):
		for i in range(self._x  ,self._x + 9):
			for j in range(self._y , self._y + 9):
				if i <= 43 and j < 1500:
					if mandalorian.ret__y() == j :
						self.decrease_boss(Board,mandalorian)
						mandalorian.delete_mand(Board)
						mandalorian.paste_mand(Board)
						mandalorian.set__activ(0)
						return



	def decrease_boss(self,Board,mandalorian):
		self.setlives(self.retlives() - 1)
		if self.retlives() == 0:
			self.boss_ac_disappear(Board)
			for i in range(5):
				Board.set_score()
			os.system('clear')
			print("You Won")
			print("Your Score" + " " + str(Board.ret_score()))
			quit()
						



