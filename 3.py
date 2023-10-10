lis_r=[]
lis_c=[]
student=int(input("Enter no of students:"))
for i in range(student):
    roll_no=int(input("Enter roll no:"))
    cgpa=float(input("Enter cgpa:"))
    lis_r.append(roll_no)
    lis_c.append(cgpa)
print("roll numbers are:",lis_r)
print("Cgpa are :",lis_c)
dic=dict(zip(lis_r,lis_c))
print(f"the dictionary is {dic}")
length_c=len(lis_c)
avg_cgpa=sum(lis_c)/length_c
print(f"Avg cgpa is:{avg_cgpa}")
lowest=min(dic.values())
highest=max(dic.values())
for i,j in dic.items():
    if j==lowest:
        print(f"lowest_cgpa={i}:{j}")
    elif j==highest:
        print(f"highest_cgpa={i}:{j}")