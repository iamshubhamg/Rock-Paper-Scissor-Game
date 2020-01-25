import random 
 
print("Please Read The Winning Rules: \n"
      "Rock vs paper    ------> paper wins \n"
      "Rock vs scissor   -----> Rock wins \n"
      "paper vs scissor  -----> scissor wins \n"
      "SO TAKE YOUR CHOICE WISELY :) \n")
while True: 
    print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n")  
    choice = int(input("User turn: "))  #we_took_input
    while choice > 3 or choice < 1: 
        choice = int(input("enter valid input: ")) 
if choice == 1: 
        choice_name = 'Rock'
    elif choice == 2: 
        choice_name = 'paper'
    else: 
        choice_name = 'scissor'
        print("user choice is: " + choice_name) 
    print("\nNow its computer turn.......") 
    comp_choice = random.randint(1, 3) 
     while comp_choice == choice: 
        comp_choice = random.randint(1, 3) 
         if comp_choice == 1: 
        comp_choice_name = 'Rock'
    elif comp_choice == 2: 
        comp_choice_name = 'paper'
    else: 
        comp_choice_name = 'scissor'
          
    print("Computer choice is: " + comp_choice_name) 
  
    print(choice_name + " V/s " + comp_choice_name) 
  #condition for winning