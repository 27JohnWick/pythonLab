D1 = {1:40, 2:70, 3:70}
D2 = {1:40, 2:50, 3:60}
D3 = {1:70, 2:80, 3:90}
marks = {"Suniti": D1, "Ryna": D2, "Ziva": D3}
highest_mark = max([marks["Suniti"][3], marks["Ryna"][3], marks["Ziva"][3]])
print(highest_mark)
