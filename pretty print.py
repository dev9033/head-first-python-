# pprint module and nested dictionary
import pprint

people = {}
people['Ford'] = {'Name': 'Ford Perfect',   'Gender': 'Male',
                  'Occupation': 'Researcher', 'Home planet': 'Betelgeuse Seven'}
people['Arthur'] = {'Name': 'Arthur Dent', 'Gender': 'Male',
                    'Occupation': 'Sandwich-maker', 'Home planet': 'Earth'}
people['Trillian'] = {'Name': 'Tricia McMillan', 'Gender': 'Female',
                      'Occupation': 'Mathematician', 'Home planet': 'Earth'}
people['Trillian'] = {'Name': 'Marvin', 'Gender': 'unknown',
                      'Occupation': 'Paranoid Android', 'Home planet': 'Unknown'}
print(people)

pprint.pprint(people)

# using double square brackets we can access the data of the perticular data
print(people['Arthur']['Occupation'])
