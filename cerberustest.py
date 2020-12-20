from cerberus import Validator


schema = {'name': {'type': 'string'}}
v = Validator(schema)

document = {'name': 'hello'}

print(type(document['name']))

if v.validate(document):
    print('data is valid')
else:
    print('invalid data')