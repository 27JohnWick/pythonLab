sample_dict = {'Physics': 82, 'Math': 65, 'history': 75}
result = min(sample_dict, key=sample_dict.get)
print(result)
