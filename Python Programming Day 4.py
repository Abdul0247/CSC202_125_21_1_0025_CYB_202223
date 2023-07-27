import random
random.seed(123)
random_integer = random.randint(1,10)
print(random_integer)

random_float = random.random( )*5
print(random_float)

loveScore= random.randint(1,100)
print(f"Your love score is {loveScore}")

random_side =random.randint(0,1)
if random_side ==1:
    print("Heads")
else:
    print("Tails")
staets_of_America=["Delaware", "New york", "Ohio", "indiana"]
staets_of_America[2]="Alabama"
staets_of_America.extend(["Angelaland", "Jack Beuer Land"])
print(staets_of_America)

user_choice= input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors.\n")
computer_choice = random.randint(0,2)
print(f"Computer choose {computer_choice}")
if user_choice==0 and computer_choice==2:
    print("You win")
elif computer_choice==0 and user_choice==2:
    print("You lose")
elif computer_choice > user_choice:
    print("You lose")
elif computer_choice==user_choice:
    print("It's a draw")
elif user_choice>=3 or user_choice<0:
     print("your input is invalid, you lose ")
else:
    print("your type in is invalid, you lose")
 
