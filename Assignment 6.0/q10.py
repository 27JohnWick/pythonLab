sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
keys = ["name", "salary"]
for key in keys:
    del sample_dict[key]
print(sample_dict)
