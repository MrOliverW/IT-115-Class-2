#Imports the JSON library
import json


#Creates the data dictonary

data = {

    'name': 'John Doe',
    'age': '30',
    'city': 'New York, NY',
    'interests': ['Bowling','jogging','gaming'],
    'is_student': True
}

#
with open('data.json','w') as json_file:

    json.dump(data,json_file,indent=4)

print('Data has been written to data.json')


#
with open('data.json','r') as json_file:

    loaded_data = json.load(json_file)

print("Successfully able to read data.json")
print(loaded_data)