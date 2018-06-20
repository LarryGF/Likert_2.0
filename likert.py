import eel
import json
import os
from functions import *

os.makedirs('data', exist_ok=True)
data_dir = os.path.join(os.path.abspath('.'),'data')



eel.init('web')

@eel.expose
def save(table,lista,last_id):
	dic = {}
	file = os.path.join(data_dir,table+'.json')
	file = open(file,'w')
	try:
		for row in lista:
			dic[row['id']] = row

		json.dump(dic,file)

		file2 = os.path.join(data_dir,'last.json')
		file2 = open(file2,'w')
		dic = {'last_id':last_id}
		json.dump(dic,file2)
		return 'Success'
	except Exception as e:
		return e

@eel.expose
def load():
	list_to_send = []
	file = os.path.join(data_dir,'objective.json')
	try:
		file = open(file)
		dic = json.load(file)
		file.close()
		lista = []
		for fila in dic.keys():
			lista.append(dic[fila])
		list_to_send.append(lista)
	except:
		list_to_send.append([])


	file = os.path.join(data_dir,'criterion.json')
	try:
		file = open(file)
		dic = json.load(file)
		file.close()
		lista = []
		for fila in dic.keys():
			lista.append(dic[fila])
		list_to_send.append(lista)
	except:
		list_to_send.append([])
	


	file = os.path.join(data_dir,'last.json')
	try:
		file = open(file)
		dic = json.load(file)
		file.close()
		last_id = dic['last_id']
		list_to_send.append(last_id)
	except:
		list_to_send.append(0)
	return list_to_send

@eel.expose
def delitems(lista,last_id):
	file = os.path.join(data_dir,'objective.json')
	try:
		file = open(file)
	except:
		return 'You must add some data before you can delete it :)'
	objective = json.load(file)
	file.close()

	file = os.path.join(data_dir,'criterion.json')
	try:
		file = open(file)
	except:
		return 'You must add some data before you can delete it :)'
	
	criterion = json.load(file)
	file.close()

	
	if str(lista[0]['id']) in objective.keys():
		print(lista)
		for dic in lista:
			print(dic['id'])
			objective.pop(str(dic['id']))

		return objective


	elif str(lista[0]['id']) in criterion.keys():
		print('criterion')

	else:
		return 'It seems like I screwed up, send me an email so I can fix it'

eel.start('likert1.html')
