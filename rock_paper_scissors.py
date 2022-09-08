import random
import sys
print("**********ROCK-PAPER-SCISSORS**********")
computerChoices = ["r", "p", "s"]
w = 0 # win
l = 0 # loss
t = 0 # tie
while True:
    print(str(w) + " Wins, " + str(l) + " Losses, " + str(t) + " Ties")
    print("Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit")
    selection = ""
    selection = input()
    while not (selection == "r" or "p" or "s" or "q"):
        print("Unknown command. Please type 'r', 'p', 's' or 'q'.")
        selection = input()
    if selection == "r":
        print("ROCK versus...")
    elif selection == "p":
        print("PAPER versus...")
    elif selection == "s":
        print("SCISSORS versus...")
    elif selection == "q":
        print("Get out of here!")
        sys.exit()  
    computerChoice = random.choice(computerChoices)
    if computerChoice == "r":
        print("ROCK")
    elif computerChoice == "p":
        print("PAPER")
    elif computerChoice == "s":
        print("SCISSORS") 
    win = "You win!"
    loss = "Haha :) LOSER!"  
    if computerChoice == selection:
        print("İt's a tie!")
        t += 1
    elif computerChoice == "r" and selection == "p":
        print(win) 
        w += 1
    elif computerChoice == "p" and selection == "r":
        print(loss) 
        l += 1
    elif computerChoice == "s" and selection == "r":
        print(win)
        w += 1
    elif computerChoice == "r" and selection == "s":
        print(loss)
        l += 1  
    elif computerChoice == "s" and selection == "p":
        print(loss)
        l += 1   
    elif computerChoice == "p" and selection == "s":
        print(win)
        w += 1             
         
        
             
                      