import random
r= random.randint(1,10) 
print("THIS IS A NUMBER GUESSSING GAME")

while True:
    userchoice=int(input("ENTER YOUR GUESS between 1 to 10:"))

    if (userchoice==r):
     print("CORRECT GUESS")
     break 
   
    elif(userchoice <r):
       print("GUESS TOO LOW ")

    else:
       print("GUESS TOO HIGH")
      
            
print ("----------GAME OVER TRY AGAIN---------------")