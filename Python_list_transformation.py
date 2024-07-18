#Question1

#Python List Transformation

#Objective: The aim of this assignment is to practice advanced list operations and transformations.

""" Problem Statement: You've been given a list of numerical grades from a class exam. You need to process and analyze these grades.


Task 1: Given the list of grades, Sort the grades in descending order and display the sorted list. """

print("="*60)

grades=[85, 90, 78, 88, 76, 95, 89, 80, 72, 93] 
print("non-sorted list: ", grades)#non-sorted list

#sorting of list in descending order:
grades.sort(reverse=True) 
print("sorted list in descending order:  ",grades)

print("="*60)
print("="*60)


""" Task 2: Calculate the average grade from the list above and display it (reminder: The average is calculated by dividing the sum of all grades by the length of the grades list). """

#Totaling the sum of the "grades"list

grades_sum = sum(grades) #naming the sum/total list
print("Sum of all grades are = ", grades_sum) 

#calculating the avergage of the grades list
grades_lenght = len(grades) #number of students
print("With a total of",grades_lenght, "students")

print("="*60)

grades_average = (grades_sum/len(grades)) #caculating the avergae grade among the students

print( "Average grade of the students are", grades_sum,"/", grades_lenght, "=", grades_average)

print("="*60)

