from view import *
from character import *
from collection import *
from affect import *
def attraction(magnet,mandalorian,Board,sh,dum,dum2):
	mandalorian.delete_mand(Board)
	if 150 - mandalorian.rety() <= 20 and 150 - mandalorian.rety() >= 0:
		if mandalorian.rety() + 5 < Board.ret_presyp() and mandalorian.rety() + 5 > Board.ret_presy():
			mandalorian.sety(mandalorian.rety() + 5)
			collection_coins(Board,mandalorian,dum)
			touch_beam(Board,mandalorian,dum2,sh)
		else :
			mandalorian.sety(Board.ret_presyp())
			collection_coins(Board,mandalorian,dum)
			touch_beam(Board,mandalorian,dum2,sh)

	elif 150 - mandalorian.rety() >= - 20 and 150 - mandalorian.rety() <= 0:
	
		if mandalorian.rety() - 5 < Board.ret_presyp() and mandalorian.rety() - 5 > Board.ret_presy():
			mandalorian.sety(mandalorian.rety() - 5)
			collection_coins(Board,mandalorian,dum)
			touch_beam(Board,mandalorian,dum2,sh)
		else :
			mandalorian.sety(Board.ret_presy())
			collection_coins(Board,mandalorian,dum)
			touch_beam(Board,mandalorian,dum2,sh)


	if 450 - mandalorian.rety() <= 20 and 450 - mandalorian.rety() >= 0:
		if mandalorian.rety() + 5 < Board.ret_presyp() and mandalorian.rety() + 5 > Board.ret_presy():
			mandalorian.sety(mandalorian.rety() + 5)
			collection_coins(Board,mandalorian,dum)
			touch_beam(Board,mandalorian,dum2,sh)

		else:
			mandalorian.sety(Board.ret_presyp())
			collection_coins(Board,mandalorian,dum)
			touch_beam(Board,mandalorian,dum2,sh)


	elif 450 - mandalorian.rety() >= - 20 and 450 - mandalorian.rety() <= 0:
	
		if mandalorian.rety() - 5 < Board.ret_presyp() and mandalorian.rety() - 5 > Board.ret_presy():
			mandalorian.sety(mandalorian.rety() - 5)
			collection_coins(Board,mandalorian,dum)
			touch_beam(Board,mandalorian,dum2,sh)
		else :
			mandalorian.sety(Board.ret_presy())
			collection_coins(Board,mandalorian,dum)
			touch_beam(Board,mandalorian,dum2,sh)

		


