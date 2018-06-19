import eel
import json
from functions import *

eel.init('web')


@eel.expose
def load():
	data = load_data()
	return data


@eel.expose
def save(name, dic):
	# print(name, dic, existing)
	result =  new_user(name, dic)
	return result

@eel.expose
def delete(user):
	result = remove_user(user)
	return result

@eel.expose
def load_table():
	table = send_table()
	print(table)
	return table


eel.start('likert1.html')
