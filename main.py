from functions import *

dic ={'criticidad':[5],'eficiencia':[5,1,2,4],'agilidad':[3,2,4,5],'innovacion':[3,2,5,1],'criterio':[5,4,5,2,1,4,3,2,5,1,4]}
users = load_data()
users = new_user('loren',dic,users)
limits = calculate_limits(users)
save_data(users)
# calculate_element('criticidad',0,users,limits)
final = calculate_total(users,limits)
print(final)
# final = calculate_total('eficiencia',3,users,limits)
# print(final)