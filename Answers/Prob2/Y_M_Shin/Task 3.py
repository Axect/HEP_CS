# -*- coding: utf-8 -*-
"""
Task 2

https://arstechnica.com/science/2014/05/win-at-rock-paper-scissors-by-knowing-thy-opponent/
"""
import random as rd

options = ["rock", "scissors", "paper"]
victorycount = 0

def WinLoss(a, b): # Determine win/loss between two variables a, b
    if  a == b:
        return 2
    elif a == "rock" and b == "scissors":
        return 1
    elif a == "rock" and b == "papaer":
        return 0
    elif a == "scissors" and b == "paper":
        return 1
    elif a == "scissors" and b == "rock":
        return 0
    elif a == "paper" and b == "rock":
        return 1
    else:
        return 0
    
def Numtoword(n): # Transfer 0, 1, 2 to rock, scissors, paper
    if n == 0:
        return "rock"
    elif n == 1:
        return "scissors"
    else:
        return "paper"

def Wordtonum(m): # Transfer rock, scissors, paper to 0, 1, 2
    if m == "rock":
        return 0
    elif m == "scissors":
        return 1
    else:
        return 2

def NextChoice(n): # n has 80% probability, rest 10% each
    inital = rd.random()
    temp = rd.random()
    b = (n+2) % 3
    c = (n+2) % 3
    if 0 <= inital and inital < 0.8:
        return options[n]
    else:
        if 0 <= temp and temp < 0.5:
            return options[b]
        else:
            return options[c]

for i in range(1,10): #Total round 9
    print("----------------------------------------------------")
    print("[Round", i, ": Choose between rock, scissors, paper]")
    choice = input("Your choice: ") # Input rock or scissors or paper
    memory = choice
    memorynum = Wordtonum(memory)

    
    if choice != "rock" and choice != "scissors" and choice != "paper":
        print("Invalid!")# If input is wrong, print invalid!
        
    else:
        if i == 1: #Round one only
            init = rd.randrange(0,3) # Computer has decided its pick
            result = WinLoss(choice, Numtoword(init)) # and result is out
            print("Computer chose", Numtoword(init))
            
            if result == 1: # If player has won
                print("You won!\n")
                victorycount = victorycount + 1
            elif result == 0: # If player has lost
                print("You lost!\n")
            elif result == 2: # If draw has occured
                print("Draw\n")
                
        else:
            if result == 1: # Previously computer has lost
                comnext = NextChoice((memorynum + 2) % 3) # Computer has decided its pick
            elif result == 0: # Previously computer has won
                comnext = NextChoice((memorynum + 1) % 3) # Computer has decided its pick
            elif result == 2: # Previously draw has occured
                comnext = Numtoword(rd.randrange(0,3)) # Computer has decided its pick
                
            result = WinLoss(choice, comnext) # and NEW result is out
            print("Computer chose", comnext)
            
            if result == 1: # If player has won
                print("You won!\n")
                victorycount = victorycount + 1
            elif result == 0: # If player has lost
                print("You lost!\n")
            elif result == 2: # If draw has occured
                print("Draw\n")
                
print("\nDuel has ended")
print("Your performance:", victorycount,"wins out of 9")