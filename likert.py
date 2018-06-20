import eel
import json
import os
from functions import *

os.makedirs('data', exist_ok=True)
data_dir = os.path.join(os.path.abspath('.'),'data')



eel.init('web')
def to_list(dic,list_to_send):

	lista = []
	for fila in dic.keys():
		lista.append(dic[fila])
	list_to_send.append(lista)	
	return lista


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
		to_list(dic,list_to_send)
		
	except:
		list_to_send.append([])


	file = os.path.join(data_dir,'criterion.json')
	try:
		file = open(file)
		dic = json.load(file)
		file.close()
		to_list(dic,list_to_send)
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

	
	if len(lista) != 0 and str(lista[0]['id']) in objective.keys():
		
		for dic in lista:
			
			objective.pop(str(dic['id']))

		objective = to_list(objective,[])
		

		return 'objective',objective


	elif len(lista) !=0 and str(lista[0]['id']) in criterion.keys():

		for dic in lista:
			
			criterion.pop(str(dic['id']))

		criterion = to_list(criterion,[])
		

		return 'criterion',criterion

	else:
		return 'It seems like I screwed up, send me an email so I can fix it'

@eel.expose
def check(users,table_obj,table_crit,last_id):
	if users == 0 or users == None or users == '':
		return "You must have at least one user"
	list_obj = []
	list_crit = []

	for row in table_obj:
		try:
			int(row['crit1'])
		except:
			row['crit1']=0
		try:
			int(row['crit2'])
		except:
			row['crit2']=0
		try:
			int(row['crit3'])
		except:
			row['crit3']=0
		try:
			int(row['crit4'])
		except:
			row['crit4']=0
		try:
			int(row['crit5'])
		except:
			row['crit5']=0

			

		if int(row['crit1'])+int(row['crit2'])+int(row['crit3'])+int(row['crit4'])+int(row['crit5']) > int(users):
			list_obj.append(row)
		else:
			pass


	for row in table_crit:
		try:
			int(row['crit1'])
		except:
			row['crit1']=0
		try:
			int(row['crit2'])
		except:
			row['crit2']=0
		try:
			int(row['crit3'])
		except:
			row['crit3']=0
		try:
			int(row['crit4'])
		except:
			row['crit4']=0
		try:
			int(row['crit5'])
		except:
			row['crit5']=0

		if int(row['crit1'])+int(row['crit2'])+int(row['crit3'])+int(row['crit4'])+int(row['crit5']) > int(users):
			list_crit.append(row)
		else:
			pass
	if len(list_obj) != 0:
		var = delitems(list_obj,last_id)
		var = var[1]
		print(var)
		mistake=True
	elif len(list_crit) != 0:
		var2 = delitems(list_crit,last_id)
		var2 = var2[1]
		print(var2)
		mistake=True

	else:
		var = table_obj
		var2 = table_crit
		mistake = False

	var2 = table_crit
	return var,var2,mistake


eel.start('likert1.html')
