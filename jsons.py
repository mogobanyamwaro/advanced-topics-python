person = {"name":"douglas"}

import json
personJson = json.dumps(person,indent=4,separators=['; '])
print(personJson)
with open('person.json','w') as file:
    json.dump(person, file)

# decoding/deserialization

person = json.loads(personJson)
print(person)

with open('person.json','r')as file:
    person = json.load(file)

class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age



def encode_user(o):
    if isinstance(o, User):
        return {'name':o.name,'age':o.age,o.__class__.__name__:True}
    else:
        raise TypeError('object not found')

user = User('Max',22)
