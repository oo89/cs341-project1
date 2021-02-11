#Project 1 for CS 341
#Section number: 006
#Semester: Spring 2021
#Written by: Oscar Ojeda Perez, oo89 
#Instructor:  Marvin Nakayama, marvin@njit.edu
import os

sectionNumber="006"
print("Project 1 for CS 341\nSection number: " + sectionNumber + 
"\nSemester: Spring 2021\nWritten by: Oscar Ojeda Perez, oo89 \nInstructor:  Marvin Nakayama, marvin@njit.edu\n" )

def checkString(stringData):
    
    state = 0
    print("Starting state: q0")
    
    for ch in stringData :
        print("Current character: " + ch)
        
        if state == 0 : 
            
            if ch.isalpha() and ch.islower():
                state = 1
                printState(state)

def printState(state): 
    
    if state == -1: 
        print("String rejected.")
        os._exit   
    else:
        print("State: q" + str(state))
            


val = input("Would you like to enter a string? (y/n): \n")

while True: 
    if(val == 'n'):
        print("Goodbye! ")
        break
    elif(val != 'y'):
        val = input("Please enter 'y' for Yes or 'n' for No \n")
        continue
    else:
       stringData = input("Enter a string: ")
       print(stringData)
       checkString(stringData)
       break


                
            
        
    






    


