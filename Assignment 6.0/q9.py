_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
keys = ["name", "salary"]
result = {key: _dict[key] for key in keys}
print(result)
