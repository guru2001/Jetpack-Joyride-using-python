from character import *
from board import *
from colorama import Style,Fore,Back,init
from view import *
init()

def touch_beam(Board,mandalorian,beam1,sh):
	for i in range(mandalorian.retx(),mandalorian.retx() + 3):
		for j in range(mandalorian.rety(), mandalorian.rety() + 4):
			if i > 0 and i < 44 and j > 0 and  j < Board.ret_presyp():
				if Board.ret_grid()[i][j] == beam1.ret_beam() or Board.ret_grid()[i][j] == beam1.ret_beam_ends() :
					Board.ret_grid()[i][j] = " "
					
					if sh == 0:
						Board.set_lives()
					beam1.beam_disappear(mandalorian,Board)
					return

def touch_beam2(Board,mandalorian,beam1,sh):
	for i in range(mandalorian.retx() - 2,mandalorian.retx() + 3):
		for j in range(mandalorian.rety(), mandalorian.rety() + 4):
			if i > 0 and i < 44 and j > 0 and  j < Board.ret_presyp():
				if Board.ret_grid()[i][j] == beam1.ret_beam() or Board.ret_grid()[i][j] == beam1.ret_beam_ends() :
					Board.ret_grid()[i][j] = " "
					
					if sh == 0:
						Board.set_lives()
					beam1.beam_disappear(mandalorian,Board)
					return

def touch_beam3(Board,mandalorian,beam1):

	beam1.beam_disappear1(mandalorian,Board)

	