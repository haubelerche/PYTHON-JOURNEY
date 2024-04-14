if __name__ == '__main__':
    studentlist = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        studentlist.append([name,score])
     
    studentlist.sort(key=lambda x:x[1])  
    second_lowest = None
       
    for student in studentlist:
        if second_lowest is None:
            second_lowest = student[1]
        elif student[1] > second_lowest:
            second_lowest = student[1]
            break     
            
#create a list for names of students with the second lowest score
second_lowest_names=[]
#find the names corresponding to the second lowest score and add them to the list 
for student in studentlist:
    if student[1] == second_lowest:
        second_lowest_names.append(student[0])
#sort the list of names alphabetically:
second_lowest_names.sort()
#print the names from the list of names with the second lowest score
for name in second_lowest_names:
    print(name)
