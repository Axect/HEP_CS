from random import randrange
def computer():
    comresult = randrange(0,2)
    if comresult == 0:
        return "Rock"
    if comresult == 1:
        return "Scissors"
    if comresult == 2:
        return "Paper"


def fight():
    huminput = input("Rock, Scissors, Paper! ")
    computer()
    if huminput == computer():
        print("Tie! try again")
    elif huminput == "Rock":
        if computer() == "Paper":
            print("HAHA You lose!")
        else :
            print("Meh You win")
    
    elif huminput == "Scissors":
        if computer() == "Rock":
            print("HAHA You lose!")
        else :
            print("Meh You win")
    
    elif huminput == "Paper":
        if computer() == "Scissors":
            print("HAHA You lose")
        else :
            print("Meh You win")

fight()