
the_menu_list =("Roll Dice Once \n"
"Roll Dice 5 Times\n"
"Roll Dice ‘n’ Times\n"
"Roll Dice until Snake Eyes\n"
"Exit")

import random
print(the_menu_list
)
choice = input("Select an option (1-5):")

if choice == "1":
    print("works1")
elif choice == "2":
    print("works2")
elif choice == "3":
    print("works3")
elif choice == "4":
    print("works4")
elif choice == "5":
    print("works5")
else:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    sum = dice1+dice2
print(dice1,",",dice2 ,"sum:",sum)



    
  
    
