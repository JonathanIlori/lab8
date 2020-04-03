import random
Number = random.randint(1,3)
wahl = input("Pick: Rock,Paper or Scissors\n").lower()
print(wahl)
i=0
while wahl == "rock" and i==0:
    if Number == 1:
        print("Computer picked Rock, no one wins -_-")
        i+=1
    elif Number == 2:
        print("Computer picked Paper, you lose:C")
        i += 1
    elif Number == 3:
        print("Computer picked Scissors, you win !!!")
        i += 1
while wahl == "scissors" and i==0:
    if Number == 1:
       print("Computer picked Rock, you lose:C")
       i+=1
    elif Number == 2:
        print("Computer picked Paper, you win !!!")
        i += 1
    elif Number == 3:
        print("Computer picked Scissors, no one wins -_-")
        i += 1
while wahl == "paper" and i==0:
    if Number == 1:
        print("Computer picked Rock, you win !!!")
        i+=1
    elif Number == 2:
        print("Computer picked Paper, no one wins -_-")
        i += 1
    elif Number == 3:
        print("Computer picked Scissors, you lose :c")
        i += 1
