import json
import os


os.makedirs('data', exist_ok=True)
data_dir = os.path.join(os.path.abspath('.'),'data')


def to_list(dic,list_to_send):

	lista = []
	for fila in dic.keys():
		lista.append(dic[fila])
	list_to_send.append(lista)	
	return lista


def func_save(table,lista,last_id):
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


def func_load():
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


def func_del(lista,last_id):
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


def func_check(users,table_obj,table_crit,last_id):
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

	
	if len(list_obj) != 0 and len(list_crit) == 0:
		var = func_del(list_obj,last_id)
		var = var[1]
		print(var)
		mistake=True
		
	elif len(list_crit) != 0 and len(list_obj) == 0:
		var2 = func_del(list_crit,last_id)
		var2 = var2[1]
		print(var2)
		mistake=True
		

	elif len(list_obj) !=0 and len(list_crit) != 0:
		var = func_del(list_obj,last_id)
		var = var[1]
		var2 = func_del(list_crit,last_id)
		var2 = var2[1]
		mistake=True

	else:
		var = table_obj
		var2 = table_crit
		mistake = False
		

	
	return var,var2,mistake





















def calculate_limits(exisiting_users):
	val = len(exisiting_users)
	limits = {'first': val, 'second': val*2,
			  'third': val*3, 'fourth': val*4, 'fifth': val*5}
	return limits






def calculate_element(table: str, aspect: int, dic: dict, limits: dict):
	users = dic
	total = 0
	for user in users:
		user_dic = users[user]
		aspect_list = user_dic[table]
		value = aspect_list[aspect]
		value = int(value)
		# print(type(value))
		total = total + value

	if table == 'criticidad':
		if total < limits['second']:
			return (total, 'Muy Baja')

		elif total < limits['third'] or total == limits['second']:
			return (total, 'Baja')

		elif total < limits['fourth'] or total == limits['third']:
			return (total, 'Media')

		elif total < limits['fifth'] or total == limits['fourth']:
			return (total, 'Alta')

		else:
			return (total, 'Muy Alta')

	else:
		if total < limits['second']:
			return (total, 'No se toma en cuenta')

		elif total < limits['third'] or total == limits['second']:
			return (total, 'Poco importante')

		elif total < limits['fourth'] or total == limits['third']:
			return (total, 'Medianamente importante')

		elif total < limits['fifth'] or total == limits['fourth']:
			return (total, 'Sumamente importante')

		else:
			return (total, 'Indispensable')


def calculate_total(users, limits):
	final_result = {}
	user_dic = users
	limit = limits
	for categoria in dictionary:
		result_list = []
		for i in range(len(dictionary[categoria])):
			result = calculate_element(categoria, i, user_dic, limit)
			result_list.append(result)

		final_result[categoria] = result_list
	# print(final_result)
	return final_result


def send_table():
	list_to_send = []
	row = {}
	existing_users = load_data()
	limits = calculate_limits(existing_users)
	total = calculate_total(existing_users,limits)

	for user in existing_users:
		row['name'] = user
		dic=existing_users[user]
		row['criticity']=dic['criticidad']
		row['eficiency_0']=dic['eficiencia'][0]
		row['eficiency_1']=dic['eficiencia'][1]
		row['eficiency_2']=dic['eficiencia'][2]
		row['eficiency_3']=dic['eficiencia'][3]
		row['agility_0']=dic['agilidad'][0]
		row['agility_1']=dic['agilidad'][1]
		row['agility_2']=dic['agilidad'][2]
		row['agility_3']=dic['agilidad'][3]
		row['innovation_0']=dic['innovacion'][0]
		row['innovation_1']=dic['innovacion'][1]
		row['innovation_2']=dic['innovacion'][2]
		row['innovation_3']=dic['innovacion'][3]
		row['criteria_0']=dic['criterio'][0]
		row['criteria_1']=dic['criterio'][1]
		row['criteria_2']=dic['criterio'][2]
		row['criteria_3']=dic['criterio'][3]
		row['criteria_4']=dic['criterio'][4]
		row['criteria_5']=dic['criterio'][5]
		row['criteria_6']=dic['criterio'][6]
		row['criteria_7']=dic['criterio'][7]
		row['criteria_8']=dic['criterio'][8]
		row['criteria_9']=dic['criterio'][9]
		row['criteria_10']=dic['criterio'][10]
		list_to_send.append(row)
		row = {}
	# print(total)
	row['name'] = 'Sumatoria'
	dic = total
	row['criticity']=str(dic['criticidad'][0][1]) +' ('+str(dic['criticidad'][0][0])+')'
	row['eficiency_0']=str(dic['eficiencia'][0][1]) +' ('+str(dic['eficiencia'][0][0])+')'
	row['eficiency_1']=str(dic['eficiencia'][1][1]) +' ('+str(dic['eficiencia'][1][0])+')'
	row['eficiency_2']=str(dic['eficiencia'][2][1]) +' ('+str(dic['eficiencia'][2][0])+')'
	row['eficiency_3']=str(dic['eficiencia'][3][1]) +' ('+str(dic['eficiencia'][3][0])+')'
	row['agility_0']=str(dic['agilidad'][0][1]) +' ('+str(dic['agilidad'][0][0])+')'
	row['agility_1']=str(dic['agilidad'][1][1]) +' ('+str(dic['agilidad'][1][0])+')'
	row['agility_2']=str(dic['agilidad'][2][1]) +' ('+str(dic['agilidad'][2][0])+')'
	row['agility_3']=str(dic['agilidad'][3][1]) +' ('+str(dic['agilidad'][3][0])+')'
	row['innovation_0']=str(dic['innovacion'][0][1]) +' ('+str(dic['innovacion'][0][0])+')'
	row['innovation_1']=str(dic['innovacion'][1][1]) +' ('+str(dic['innovacion'][1][0])+')'
	row['innovation_2']=str(dic['innovacion'][2][1]) +' ('+str(dic['innovacion'][2][0])+')'
	row['innovation_3']=str(dic['innovacion'][3][1]) +' ('+str(dic['innovacion'][3][0])+')'
	row['criteria_0']=str(dic['criterio'][0][1]) +' ('+str(dic['criterio'][0][0])+')'
	row['criteria_1']=str(dic['criterio'][1][1]) +' ('+str(dic['criterio'][1][0])+')'
	row['criteria_2']=str(dic['criterio'][2][1]) +' ('+str(dic['criterio'][2][0])+')'
	row['criteria_3']=str(dic['criterio'][3][1]) +' ('+str(dic['criterio'][3][0])+')'
	row['criteria_4']=str(dic['criterio'][4][1]) +' ('+str(dic['criterio'][4][0])+')'
	row['criteria_5']=str(dic['criterio'][5][1]) +' ('+str(dic['criterio'][5][0])+')'
	row['criteria_6']=str(dic['criterio'][6][1]) +' ('+str(dic['criterio'][6][0])+')'
	row['criteria_7']=str(dic['criterio'][7][1]) +' ('+str(dic['criterio'][7][0])+')'
	row['criteria_8']=str(dic['criterio'][8][1]) +' ('+str(dic['criterio'][8][0])+')'
	row['criteria_9']=str(dic['criterio'][9][1]) +' ('+str(dic['criterio'][9][0])+')'
	row['criteria_10']=str(dic['criterio'][10][1]) +' ('+str(dic['criterio'][10][0])+')'
	
	list_to_send.append(row)
	return list_to_send

		
