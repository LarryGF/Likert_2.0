import json
dictionary = {'criticidad': [1, ], 'eficiencia': [5, 1, 2, 4], 'agilidad': [
	3, 2, 4, 5], 'innovacion': [3, 2, 5, 1], 'criterio': [5, 4, 5, 2, 1, 4, 3, 2, 5, 1, 4]}

try:
	file = open('users.json')
	# exisiting_users = json.load(file)

except:
	file = open('users.json', 'w')
	file.write("{}")
	file.close()


def calculate_limits(exisiting_users):
	val = len(exisiting_users)
	limits = {'first': val, 'second': val*2,
			  'third': val*3, 'fourth': val*4, 'fifth': val*5}
	return limits

def remove_user(user):
	try:	
		existing_users = load_data()
		existing_users.pop(user)
		save_data(existing_users)
	except Exception as e:
		return e
	return 'Succes'
	
def new_user(name: str, dic: dict):
	existing_users= load_data()
	existing_users[name] = dic
	# print(existing_users)
	# return exisiting_users
	save_data(existing_users)
	return 'Success'


def load_data():
	file = open('users.json')
	users = json.load(file)
	return users


def save_data(exisiting_users):
	file = open('users.json', 'w')
	json.dump(exisiting_users, file)
	file.close()
	return "Success"


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

		
