#1
###########################################################
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


x[1][0] = 15
print(x)


students[0].update({"last_name" : "Bryant"})
print(students)


sports_directory['soccer'][0]= "Andres"
print(sports_directory)



z[0]['y']= 30
print(z)





#2
##############################################
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary(dict):
    for i in range(0,len(dict)):
        print("first_name - " + dict[i]['first_name'] + ", last_name - " + dict[i]['last_name'])
iterateDictionary(students)



#3
####################################################
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary2(key_name, some_list):
    for i in some_list:
        print(i[key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)


#4
##################################################
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    print(f"{len(some_dict['locations'])} LOCATIONS")
    for i in range(0,len(some_dict['locations'])):
        print(some_dict['locations'][i])
    print(f"{len(some_dict['instructors'])} INSTRUCTORS")
    for i in range(0,len(some_dict['instructors'])):
        print(some_dict['instructors'][i])

printInfo(dojo)



