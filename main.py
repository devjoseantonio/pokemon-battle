#Importin library to use random numbers
from random import randint 

#Rival's pokemon Health Points
rival_hp =  80
#My pokemon's Health Points
my_hp = 90

#Battle cycle
while rival_hp > 0 and my_hp > 0:
    #Pokemons life
    print("Rival's pikachu life is: {}, your squirtle's life is {}".format(rival_hp, my_hp))
    #Rival's turn
    print("Your rival's turn")
    input("Press enter to continue...")
    rival_atk = randint(0, 1)
    #If the rival attack is 0 then uses electro ball otherwise uses thunder wave
    if(rival_atk == 0):
        print("Pikachu uses Electro Ball -20")
        my_hp -= 20
    else:
        print("Pikachu uses Thunder Wave -10")
        my_hp -= 10
    input("Press enter to continue...")
    #Your turn
    print("It's your turn wich attack do you want to use?:")
    print("0. Tackle -- atk 10")
    print("1. Water gun -- atk 15")
    print("2. Bubble -- atk 20")
    my_atk = -1
    #Repeats until select a valid option
    while my_atk < 0 or my_atk > 2:
        my_atk = input("Select an option: ")
        #Check if the attack selected is not a number
        if not my_atk.isnumeric():
            print("Error: Select a numeric option")
            my_atk = -1
        else:
            my_atk = int(my_atk)
            #check wich attack I am using
            match my_atk:
                case 0:
                    print("Squirtle uses Tackle")
                    rival_hp -= 10
                case 1:
                    print("Squirtle uses Water gun")
                    rival_hp -= 15
                case 2:
                    print("Squirtle uses Bubble")
                    rival_hp -= 20
                #Check if the attack selected is a valid option
                case _:
                    print("Error: select a number between 0-2")
    input("Press enter to continue...")
if rival_hp >= 0:
    print("Rival's pikachu has fainted, you win !")
else:
    print("Your squirtle has fainted. Going to a pokemon center")