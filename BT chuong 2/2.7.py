import json

json_data = '{"name": "MinhVu", "age": 20, "city": "Hanoi"}'
python_obj = json.loads(json_data)
print(python_obj)