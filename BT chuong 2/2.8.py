import json

python_obj = {'name': 'MinhVu', 'age': 21, 'city': 'Hanoi'}
json_data = json.dumps(python_obj, indent=4)
print(json_data)