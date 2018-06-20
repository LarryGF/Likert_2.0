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
	except:
		return [[],[],0]
	dic = json.load(file)
	file.close()
	lista = []
	for fila in dic.keys():
		lista.append(dic[fila])
	list_to_send.append(lista)


	file = os.path.join(data_dir,'criterion.json')
	try:
		file = open(file)
	except:
		return [[],[],0]
	
	dic = json.load(file)
	file.close()
	lista = []
	for fila in dic.keys():
		lista.append(dic[fila])
	list_to_send.append(lista)


	file = os.path.join(data_dir,'last.json')
	file = open(file)
	dic = json.load(file)
	file.close()
	last_id = dic['last_id']
	list_to_send.append(last_id)

	return list_to_send


	# with open('{}.json'.format(table)) as f:
	# 	dic = json.load(f)
	# 	lista = []
	# 	for fila in sorted(dic.keys()):  ####ordenar las filas al ingresarlas a la lista
	# 		lista.append(dic[fila])
	# print(lista)
	# return lista



eel.start('likert1.html')
