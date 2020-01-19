import random 
 
print("Please Read The Winning Rules: \n"
      +"Rock vs paper->paper wins \n"
      + "Rock vs scissor->Rock wins \n"
      +"paper vs scissor->scissor wins \n") 
  
while True: 
    print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n")  
    choice = int(input("User turn: "))  #we_took_input
    while choice > 3 or choice < 1: 
        choice = int(input("enter valid input: ")) 
