from character import *
from board import *
from colorama import Style,Fore,Back,init
from view import *
init()

def collection_coins(Board,mandalorian,coin1):
	
	for i in range(mandalorian.retx(),mandalorian.retx() + 3):
		for j in range(mandalorian.rety(), mandalorian.rety() + 4):
			if i > 0 and i < 44 and j > 0 and  j < Board.ret_presyp():
				if Board.ret_grid()[i][j] == coin1.retcoins():
					Board.ret_grid()[i][j] = " "
					Board.set_score()

def collection_coins2(Board,mandalorian,coin1):
	
	for i in range(mandalorian.retx() - 2,mandalorian.retx() + 3):
		for j in range(mandalorian.rety(), mandalorian.rety() + 4):
			if i > 0 and i < 44 and j > 0 and  j < Board.ret_presyp():
				if Board.ret_grid()[i][j] == coin1.retcoins():
					Board.ret_grid()[i][j] = " "
					Board.set_score()
				

