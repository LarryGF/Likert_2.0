import eel
import json
import os
from functions import *

eel.init('web')


@eel.expose
def save(table,lista,last_id):
	result = func_save(table,lista,last_id)
	return result
	

@eel.expose
def load():
	result = func_load()
	return result
@eel.expose
def delitems(lista,last_id):
	result = func_del(lista,last_id)
	return result

	
@eel.expose
def check(users,table_obj,table_crit,last_id):
	result = func_check(users,table_obj,table_crit,last_id)
	return result
	

eel.start('likert1.html')
