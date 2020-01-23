from colorama import init
init()
from colorama import Fore,Style,Back
import time
import os
class Board:
	def __init__(self,leng,wid):
		self.__presyl = 0
		self.__presyp = 0
		self.__leng = leng
		self.__wid = wid
		self.__grid = [[" "for x in range(self.__wid)] for y in range(self.__leng)]
		self.__sky = Fore.CYAN + Back.BLUE + Style.BRIGHT + "~" + Style.RESET_ALL
		self.__ground = Fore.GREEN + Style.BRIGHT +  "_" +   Style.RESET_ALL
		self.__ground1 = Fore.BLACK + Style.BRIGHT + Back.RED +  "|"  + Style.RESET_ALL
		self.__start_time = time.time()
		self.__lives = 5

		self.__score = 0
		self.__time = 180
	
	def ret_stime(self):
		return self.__start_time
	
	def ret_len(self):
		return self.__leng
	def ret_lives(self):
		return self.__lives
	def ret_score(self):
		return self.__score
	
	def set_lives(self):
		self.__lives = self.__lives - 1
	
	def set_score(self):
		self.__score = self.__score + 5

	def ret_wid(self):
		return self.__wid

	def ret_grid(self):
		return self.__grid
	def ret_presy(self):
		return self.__presyl

	def set_presy(self,x):
		self.__presyl = x
	
	def ret_presyp(self):
		return self.__presyp

	def set_presyp(self,x):
		self.__presyp = x

	
	def create_sky(self):
		for i in range(self.__wid):
			for j in range(3):
				self.__grid[j][i] = self.__sky

	def create_ground(self):
		for i in range(self.__wid):
			self.__grid[self.__leng - 3][i] = self.__ground

		for i in range(self.__leng - 2,self.__leng):
			for j in range(self.__wid):
				self.__grid[i][j] = self.__ground1


	def printit(self,sh2,mandalorian):
		if sh2 == 1:
			self.set_presy(self.ret_presy() + 3)
			self.set_presyp(self.ret_presy() + 210)
			if mandalorian.rety() <= 1310:
				string = ""
				string = string + "Lives: " + str(self.__lives) + "                   "
				string = string + "Score: " +  str(self.__score) + "                    "
				string = string + "Time Remaining: " + str(self.__time - int(time.time() - self.__start_time)) +  "\n"  
				if self.__time - int(time.time() - self.__start_time) <= 0:
					os.system('clear')
					print("Time Up")
					quit()
				if self.__lives == 0:
					os.system('clear')
					print("You are Dead")
					quit()
				
				for i in range(49):
					for j in range(self.ret_presy(), self.ret_presyp()):
						string = string + self.__grid[i][j]
					string = string + "\n"
				print(string)	
				string =""

		elif sh2 == 0:
			self.set_presy(self.ret_presy() + 1)
			self.set_presyp(self.ret_presy() + 210)
			if self.ret_presyp() >= 1499:
				self.set_presyp(1499)
			if mandalorian.rety() <= 1310 :
				string = ""
				string = string + "Lives: " + str(self.__lives) + "                   "
				string = string + "Score: " +  str(self.__score) + "                    "
				string = string + "Time Remaining: " + str(self.__time - int(time.time() - self.__start_time)) +  "\n"  
				if self.__time - int(time.time() - self.__start_time) <= 0:
					os.system('clear')
					print("Time Up")
					quit()
				if self.__lives == 0:
					os.system('clear')
					print("You are Dead")
					quit()
				
				for i in range(49):
					for j in range(self.ret_presy(), self.ret_presyp()):
						string = string + self.__grid[i][j]
					string = string + "\n"
				print(string)	
				string =""
		else: 
			self.printit2(sh2)		

	def printit2(self,sh2,mandalorian):
		self.set_presy(1290)
		self.set_presyp(1499)
		if mandalorian.rety() > 1310:
			string = ""
			string = string + "Lives: " + str(self.__lives) + "                   "
			string = string + "Score: " +  str(self.__score) + "                    "
			string = string + "Time Remaining: " + str(self.__time - int(time.time() - self.__start_time)) +  "\n"  
			if self.__time - int(time.time() - self.__start_time) <= 0:
				os.system('clear')
				print("Time Up")
				quit()
			if self.__lives == 0:
				os.system('clear')
				print("You are Dead")
				quit()
			for i in range(49):
				for j in range(1290 , 1500):	
					string = string + self.__grid[i][j]
				string = string + "\n"
			print(string)
			string = ""
		else:
			string = ""
			string = string + "Lives: " + str(self.__lives) + "                   "
			string = string + "Score: " +  str(self.__score) + "                    "
			string = string + "Time Remaining: " + str(self.__time - int(time.time() - self.__start_time)) +  "\n"  
			if self.__time - int(time.time() - self.__start_time) <= 0:
				os.system('clear')
				print("Time Up")
				quit()
			if self.__lives == 0:
				os.system('clear')
				print("You are Dead")
				quit()
			for i in range(49):
				for j in range(1290 , 1500):	
					string = string + self.__grid[i][j]
				string = string + "\n"
			print(string)
			string = ""

