# in dictionary we have key value pairs
# key -> value e.g. {name : "John Doe", age: 23 }

# db = {
#     'name': 'John Doe',
#     'age': 27,
#     'DOB': '01/01/1995'
# }
# print(db['name'])
# print(db.keys())


# '''adding entries to the dictionary'''
# # db['name'].append('Kelly')  # append only works with list
# # db['age'].append(32)  # append only works with list

# db.update({'name':'Kelly'})
# db.update({'age':44})

# print(db)

# del db['name']
# print(db)
'''deleting from a dictionary using a for loop'''
db = {}

db.update({'name': ['John Doe', 'Kelly Morgan']})
db.update({'age': [24, 23]})

index = db['name'].index('John Doe')

for value in db.values():
    for subvalue in value:
        print(subvalue)


for key in db.keys():
    del db[key][index]

print(db)
