
the_menu_list =("\n""MAIN MENU\n""Roll Dice Once \n"
"Roll Dice 5 Times\n"
"Roll Dice ‘n’ Times\n"
"Roll Dice until Snake Eyes\n"
"Exit")
sum = 0
def roll_one_dice():
    
    global sum
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    sum = dice1+dice2
    print(dice1,",",dice2,"sum:",sum,)
import random

      
def begin_loop():
    global sum
    print(the_menu_list)

    choice = input("Select an option (1-5):")

    if choice == "1":
        roll_one_dice()
        begin_loop()
    elif choice == "2":
        i = 0
        while i < 5:
            i +=1
            roll_one_dice()
        begin_loop()
    elif choice == "3":
        number_of_times = int(input("input the # of times you want to roll:"))
        i = 0
        while i < number_of_times:
            i +=1
            roll_one_dice()
        begin_loop()
    elif choice == "4":
    
        i = 0
        while sum != 2:
            i+= 1
            roll_one_dice()
        sum = 0  
        print("you rolled",i,"times")
        begin_loop()

            
    elif choice == "5":
        print("task_ended")
begin_loop()        
   
    




    
  
    
