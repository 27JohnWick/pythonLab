import random
li=[]
print("Random integers between 0 and 9: ")
for ele in range(4, 15):
     el= random.randrange(9)
     li.append(el)

print("The list generated from random number is ",li)
