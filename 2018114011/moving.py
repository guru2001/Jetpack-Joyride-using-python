import signal
from alarm import AlarmException
from get import _getChUnix as getChar
import time
from character import *
import os
from board import *
from collection import *
from shield import *
from affect import *
sh = Shield()
def mandamove(mandalorian,Board,dum,dum2,villain):
	sh.check1(mandalorian,Board)
	start = 0
	def alarmhandler(signum, frame):
		raise AlarmException

	def user_input(timeout=0.15):
		''' input method '''
		signal.signal(signal.SIGALRM, alarmhandler)
		signal.setitimer(signal.ITIMER_REAL, timeout)
		
		try:
			text = getChar()()
			signal.alarm(0)
			return text
		except AlarmException:
			pass
		signal.signal(signal.SIGALRM, signal.SIG_IGN)
		return ''
	

	def gravity(mandalorian,Board,dum,dum2):
		i = int(mandalorian.retx()//12)
		if mandalorian.retx() + (i+2) < 44:
			mandalorian.setx(mandalorian.retx() + (i+2) )
			collection_coins2(Board,mandalorian,dum)
			touch_beam2(Board,mandalorian,dum2,sh.retact())
		else:
			mandalorian.setx(43)
			collection_coins2(Board,mandalorian,dum)
			touch_beam2(Board,mandalorian,dum2,sh.retact())

	def gravity1(mandalorian,Board,dum,dum2):
		mandalorian.delete_mand(Board)

		i = int(mandalorian.retx()//12)
		if mandalorian.retx() + (i//4+1) < 44:
			mandalorian.setx(mandalorian.retx() + (i//4 + 1))
			collection_coins(Board,mandalorian,dum)
			touch_beam(Board,mandalorian,dum2,sh.retact())
		else:
			mandalorian.setx(43)
			collection_coins(Board,mandalorian,dum)
			touch_beam(Board,mandalorian,dum2,sh.retact())
	
	char = user_input()

	if char == "q":
		os.system('clear')
		quit()

	elif char == "w":
		mandalorian.delete_mand(Board)
		if mandalorian.retx() >= 8 and mandalorian.retx() < 45:
			mandalorian.setx(mandalorian.retx() - 5)
			
			if sh.retact() == 1:
				mandalorian.ret_upshield()

			else:
				mandalorian.set_upmatrix()

			collection_coins2(Board,mandalorian,dum)
			touch_beam2(Board,mandalorian,dum2,sh.retact())

		else:
			mandalorian.setx(3)
			if sh.retact() == 1:
				mandalorian.ret_upshield()

			else:
				mandalorian.set_upmatrix()

			collection_coins2(Board,mandalorian,dum)
			touch_beam(Board,mandalorian,dum2,sh.retact())

	
		

	elif char == "d":
		gravity1(mandalorian,Board,dum,dum2)
		mandalorian.delete_mand(Board)
		if mandalorian.rety() > Board.ret_presy() - 4 and  mandalorian.rety() < Board.ret_presyp() - 4:
			mandalorian.sety(mandalorian.rety() + 5)
			if sh.retact() == 1:
				mandalorian.shield()

			else:
				mandalorian.same_matrix()	
	
		else:
			mandalorian.sety(Board.ret_presyp() - 4)
			if sh.retact() == 1:
				mandalorian.shield()

			else:
		
				mandalorian.same_matrix()

		collection_coins(Board,mandalorian,dum)
		touch_beam(Board,mandalorian,dum2,sh.retact())


	elif char == "a":
		gravity1(mandalorian,Board,dum,dum2)
		mandalorian.delete_mand(Board)

		if mandalorian.rety() > Board.ret_presy() + 2  and  mandalorian.rety() < Board.ret_presyp():
			mandalorian.sety(mandalorian.rety() - 5)
			if sh.retact() == 1:
				mandalorian.shield()

			else:
				mandalorian.same_matrix()

		else:
			mandalorian.sety(Board.ret_presy())
			if sh.retact() == 1:
				mandalorian.shield()

			else:
				mandalorian.same_matrix()

		collection_coins(Board,mandalorian,dum)
		touch_beam(Board,mandalorian,dum2,sh.retact())

	

	elif char == "e":
		if mandalorian.ret__activ() == 0:
			mandalorian.update_bx()
			mandalorian.update_by()
			mandalorian.appear(Board,villain)



	elif char == " ":
		mandalorian.delete_mand(Board)
		sh.check(mandalorian,Board)

	
	else:
		mandalorian.delete_mand(Board)
		gravity(mandalorian,Board,dum,dum2)
		if sh.retact() == 1:
			mandalorian.shield()
		else:
			mandalorian.same_matrix()
	return sh.retact()