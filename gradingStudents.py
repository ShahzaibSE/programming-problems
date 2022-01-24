def gradingStudents(grades):
    for i in range(len(grades)):
        if(grades[i] < 38):
            continue
        else:
            temp = grades[i]
            multiple_temp = grades[i] % 5
            if(multiple_temp == 3):
                temp = temp + 2
                grades[i] = temp
            elif(multiple_temp == 4):
                temp = temp + 1
                grades[i] = temp
            else:
                continue
    return grades



print(gradingStudents([4,73,67,38,33]))

# lambdaDef = lambda a : a + 1
# print(lambdaDef(1))