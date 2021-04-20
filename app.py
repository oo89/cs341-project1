#Project 1 for CS 341
#Section number: 006
#Semester: Spring 2021
#Written by: Oscar Ojeda Perez, oo89 
#Instructor:  Marvin Nakayama, marvin@njit.edu
import os
#this meth will check each state and always is going to print the initial state.
def checkString(stringData):
    
    state = 0
    print("Starting state: q0")
    #loop the string was entered
    for ch in stringData :
        print("Current character: " + ch)
        #First state that is q0 check if it is Γ
        if state == 0 : 
            if ch.isalpha() and ch.islower():
                state = 1
                printState(state)
            else: #String rejected.
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
            else:#String rejected.
                state = -1 
                printState(state)
                
        #q3 will check for Γ and if it is other will go to a trap state. 
        elif state == 3:
            if ch.isalpha() and ch.islower():
                state = 1 
                printState(state)
            # Trap State 
            else: #String rejected.
                state = 10
                printState(state)
                break
                
        #q2 check Γ or other 
        elif state == 2:
            if ch.isalpha() and ch.islower():
                state = 5 
                printState(state)
            else: #String rejected.
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
            else: #String rejected.
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
            else: #String rejected. 
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
            else:#String rejected.
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
            else:#String rejected.
                state = -1 
                printState(state)
        #q9 check Γ, ∆, trap with Φ. This is a final state (Accepting state)
        elif state == 9:
            if ch == '.':
                state = 6 
                printState(state)
            elif ch.isalpha() and ch.islower():
                state = 5 
                printState(state)
            else: #String rejected.
                state = 10 
                printState(state)
                
    # final state after the for loop 
    if state == 9: 
        print("String accepted.")
    else:
        print("String rejected.")
#Print State or string is rejected. when I said -1 is that is going to a trap state, the char is not accepted. Thas why in some cases the output finish with the char.        
def printState(state):
    if state == -1 or state == 10: 
        if state == 10: 
            print("State: q" + str(state))
            print("String rejected.")
            main()
        else:     
            print("String rejected.")
            main()
    else:
        print("State: q" + str(state))
            
#main meth to control the inputs from the user. 
def main(): 
    val = input("Would you like to enter a string? (y/n): \n")

    while True: 
        if(val == 'n'):
            print("Goodbye! ")
            exit()
        elif(val != 'y'):
            val = input("Please enter 'y' for Yes or 'n' for No \n")
            continue
        else:
            stringData = input("Enter a string: ")
            print(stringData)
            checkString(stringData)
            val = input("Would you like to enter a string? (y/n): \n")
            continue

sectionNumber="006"
print("Project 1 for CS 341\nSection number: " + sectionNumber + 
"\nSemester: Spring 2021\nWritten by: Oscar Ojeda Perez, oo89 \nInstructor:  Marvin Nakayama, marvin@njit.edu\n" )
main()
                
            
        
    






    


