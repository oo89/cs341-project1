import os

sectionNumber="006"
print("Project 1 for CS 341\nSection number: " + sectionNumber + 
"\nSemester: Spring 2021\nWritten by: Oscar Ojeda Perez, oo89 \nInstructor:  Marvin Nakayama, marvin@njit.edu\n" )

val = input("Would you like to enter a string? y or n \n")

while True: 
    if(val == 'n'):
        print("Goodbye! ")
        break
    elif(val != 'y'):
        val = input("Please enter 'y' for Yes or 'n' for No \n")
        continue
    else:
       stringData = input("enter a string over Σ: ")
       print(stringData)
       break
       
       
       






    


