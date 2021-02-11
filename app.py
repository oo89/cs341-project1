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
        #First state that is q0 check if it is Γ
        if state == 0 : 
            if ch.isalpha() and ch.islower():
                state = 1
                printState(state)
            else: # check this 
                state = -1 
                printState(state)
                
        #q1 check if it is Γ*, ∆, Φ
        elif state == 1:
            if ch.isalpha() and ch.islower():
                state = 1 
                printState(state)
            elif ch == '.':
                state = 3
                printState(state)
            elif ch == '@':
                state = 2 
                printState(state)
            else:
                state = -1 
                printState(state)
                
        #q3 will check for Γ and if it is other will go to a trap state. 
        elif state == 3:
            if ch.isalpha() and ch.islower():
                state = 1 
                printState(state)
            # Trap State 
            else: # check this 
                state = -1 
                printState(state)
                
        #q2 check Γ or other 
        elif state == 2:
            if ch.isalpha() and ch.islower():
                state = 5 
                printState(state)
            else: # check this 
                state = -1  
                printState(state)
                
        #q5 heck Γ* or ∆        
        elif state == 5:
            if ch.isalpha() and ch.islower():
                state = 5
                printState(state)
            elif ch == '.':
                state = 6
                printState(state)
            else: # check this here I could uses trap state q4
                state = -1 
                printState(state)
        #q6 check n or Γ-n          
        elif state == 6: 
            if ch == 'n':
                state = 7 
                printState(state)
            elif ch.isalpha() and ch.islower() and ch != 'n':
                state = 5 
                printState(state)
            else: # check this 
                state = -1 
                printState(state)
        #q7 check e, ∆ or Γ-e  
        elif state == 7: 
            if ch == 'e': 
                state = 8
                printState(state)
            elif ch.isalpha() and ch.islower() and ch != 'e':
                state = 5 
                printState(state)
            elif ch == '.': 
                state = 6 
                printState(state)
            else:
                state = -1 
                printState(state)
        #q8 check t, Γ-e, ∆ 
        elif state == 8: 
            if ch == 't':
                state = 9 
                printState(state)
            elif ch == '.': 
                state = 6
                printState(state)
            elif ch.isalpha() and ch.islower() and ch != 't':
                state = 5 
                printState(state)
            else:
                state = -1 
                printState(state)
        #q9 check Γ, ∆, trap with Φ. This is a final state 
        elif state == 9:
            if ch == '.':
                state = 6 
                printState(state)
            elif ch.isalpha() and ch.islower():
                state = 5 
                printState(state)
            else: # check this. here if the enter @ will brake and also other different tan the other two.
                state = 10 
                printState(state)
                
    # final state after the for 
    if state == 9: 
        print("String accepted.")
    else:
        print("String rejected.")
        
def printState(state):
    if state == -1: 
        print("String rejected.")
        exit()   
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


                
            
        
    






    


