students = ['Hao', 'Ruoxi','Iqbal','Jenny','myanmar','china']
# print(students[0])
# print(students[1])
# print(students[2])
# print(students[3])
# print(students[-1])
print(students[0:4])
print(len(students))
students[2] = 'Farah'
print(students)
del students[2]
print(students)


print("this is from for loop")
for x in range(len(students)):
    print("data: %s"%students[x])


students.append("Austrila")
students.append("japan")
print("this is from for loop append:")
for x in range(len(students)):
    print("data: %s"%students[x])
    

girl = ['japanGirl','KoeranGirl','ChinaGirl']

students.extend(girl)
print("this is from for loop extend")
for x in range(len(students)):
    print("data: %s"%students[x])