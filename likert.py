import eel
import json
import os
from functions import *

eel.init('web')


@eel.expose
def save(table,lista,last_id,values_list):
	result = func_save(table,lista,last_id,values_list)
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


@eel.expose
def run(table_obj,table_crit,users):
	result = func_run(table_obj,table_crit,int(users))
	
	return result

@eel.expose
def summary(values_list,likert_table_obj,users):
	
	result = func_summary(values_list,likert_table_obj,users)

	return result
	

eel.start('likert1.html')
