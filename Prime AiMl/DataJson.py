import json
# py_obj = {
#     "name": "Ankita",
#     "isStudent": None
# }
# json_str = json.dumps(py_obj) #dumps - py strings into Json data
# print(type(json_str), json_str)


# json_str = '{"name" : "Ankita", "isStudent" : null}'
# py_obj = json.loads(json_str) # loads create Json file into python obj
# print(type(py_obj), py_obj)

data= {
    "name " : "Anku",
    "age": 20,
    "isStudent" : True
}
with open('data.json', 'w') as f:
    json.dump(data, f, indent = 4, sort_keys = True)

# with open("data.json", "r") as f:
#     py_obj = json.load(f)
#     print(type(py_obj))