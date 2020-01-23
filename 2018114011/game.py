import os
from board import *
from character import *
from alarm import AlarmException
from get import _getChUnix as getChar
from moving import *
from view import *
from collection import *
from shield import *
from affect import *
from power import Power
from attract import attraction
os.system("clear")
board_obj = Board(49,1500)

board_obj.create_sky()
board_obj.create_ground()
all_coins = coins(board_obj)
all_coins.place()
all_beams = beams(board_obj)
all_beams.place()

magnets = magnet(board_obj)
magnets.place()

power = power_up(board_obj)
power.place()

hero = mandalorian()
hero.paste_mand(board_obj)

villain = boss_create()
villain.boss_update(board_obj)

dum3 = Power()

while 1:
	print("\033[0;0H" , end ="")
	dum3.Power_fn(board_obj,hero)
	dum3.check1(hero,board_obj)
	sh2 = dum3.retact()
	dum = coin1()
	dum2 = beam1()
	sh = mandamove(hero,board_obj,dum,dum2,villain)

	attraction(magnets,hero,board_obj,sh,dum,dum2)

	hero.update_mand(board_obj,sh2,sh,dum,dum2)	
	if hero.ret__activ() == 1:
		hero.check(board_obj,dum2,villain)
		hero.disappear(board_obj)
		hero.upgrade(board_obj,villain)
		if hero.ret__activ() == 1:
			hero.appear(board_obj,villain)
	villain.boss_movement(board_obj,hero,sh)

	add = hero.ret_add(board_obj)
	add1 = add
		
