import json
python_obj = {'name': 'MinhVu', 'age': 20, 'city': 'Hanoi'}
json_data = json.dumps(python_obj, indent=4, sort_keys=True)
print(json_data)