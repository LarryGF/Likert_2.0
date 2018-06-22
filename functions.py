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


def func_save(table,lista,last_id,values_list):
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
		dic['values_list'] = values_list
		print(dic)
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
		list_to_send.append(dic['values_list'])
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
		return (0,0,1)
	list_obj = []
	list_crit = []
	list_names = []

	for row in table_obj:
		
		row = check_existence(row)	

		if int(row['crit1'])+int(row['crit2'])+int(row['crit3'])+int(row['crit4'])+int(row['crit5']) > int(users):
			list_obj.append(row)
			list_names.append(row['name'])
		else:

			pass


	for row in table_crit:
		row = check_existence(row)
		
		if int(row['crit1'])+int(row['crit2'])+int(row['crit3'])+int(row['crit4'])+int(row['crit5']) > int(users):
			list_crit.append(row)
			list_names.append(row['name'])
		else:
			pass

	
	if len(list_obj) != 0 and len(list_crit) == 0:
		print('1')
		var = func_del(list_obj,last_id)
		var = var[1]
		var2 = table_crit
		print(var)
		mistake=True
		
	elif len(list_crit) != 0 and len(list_obj) == 0:
		print('2')
		var2 = func_del(list_crit,last_id)
		var2 = var2[1]
		var = table_obj
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
		
	return var,var2,mistake,list_names

def func_run(table_obj,table_crit,users):
	list_to_send_obj = []
	list_to_send_crit = []
	list_to_send_sum_obj = []
	limits = calculate_limits(users)
	
	for objective in table_obj:
		result = Likert_quant(objective)
		result2 = Likert_qualit(result,limits)
		dic = {"name":objective['name'],"value":result,"significance":result2,"category":objective['category'] }
		list_to_send_obj.append(dic)
	
	for criterion in table_crit:
		result = Likert_quant(criterion)
		result2 = Likert_qualit(result,limits)
		dic = {"name":criterion['name'],"value":result,"significance":result2,"category":criterion['category'] }
		list_to_send_crit.append(dic)

	for objective in table_obj:
		total = int(objective['crit1'])+ int(objective['crit2'])+ int(objective['crit3'])+ int(objective['crit4'])+ int(objective['crit5'])
		dic = {'name':objective['name'],'crit1':str(round(int(objective['crit1'])/int(total)*100))+'%','crit2':str(round(int(objective['crit2'])/int(total)*100))+'%','crit3':str(round(int(objective['crit3'])/int(total)*100))+'%','crit4':str(round(int(objective['crit4'])/int(total)*100))+'%','crit5':str(round(int(objective['crit5'])/int(total)*100))+'%'}
		list_to_send_sum_obj.append(dic)


	return list_to_send_obj,list_to_send_crit,list_to_send_sum_obj

def func_summary(values_list,likert_table_obj,users):
	list_to_send = []
	total = 0
	dic = {}
	max_value = 0
	#finding the total amount of points
	for objective in likert_table_obj:
		max_value = max_value + objective['value']



	#sanitizing the values input, I don't know much javascript so it will be done here
	new_values_list = []

	while len(values_list) != 0:
		value = values_list.pop()
		if value not in values_list:
			new_values_list.append(value)
		else:
			pass

	
	values_list = new_values_list

	#it wouldn't be a bad idea to optimize this code, by deleting the used objectives and values
	for value in values_list:
		
		for objective in likert_table_obj:
			
			if objective['category'] == value:
				total = total + int(objective['value'])

			else:
				pass

		total = str(round(int(total)/int(max_value)*100)) + '%'
		dic['name'] = value
		dic['value'] = total
		list_to_send.append(dic)
		dic = {}
		total = 0

	print(list_to_send)
	return list_to_send









def Likert_quant(objective):

	objective = check_existence(objective)
	value1 = int(objective['crit1'])
	value2 = int(objective['crit2'])
	value3 = int(objective['crit3'])
	value4 = int(objective['crit4'])
	value5 = int(objective['crit5'])
	total = 5*value5 + 4*value4 + 3*value3 + 2*value2 + value1
	return total

def Likert_qualit(result,limits):

	if result < limits['second']:
			return ('No Significance')

	elif result < limits['third'] or result == limits['second']:
		return ('Low Significance')

	elif result < limits['fourth'] or result == limits['third']:
		return ('Mild Significance')

	elif result < limits['fifth'] or result == limits['fourth']:
		return ('High Significance')

	else:
		return ('Very High Significance')




def check_existence(row):
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

	return row




def calculate_limits(exisiting_users):
	val = exisiting_users
	limits = {'first': val, 'second': val*2,
			  'third': val*3, 'fourth': val*4, 'fifth': val*5}
	return limits



