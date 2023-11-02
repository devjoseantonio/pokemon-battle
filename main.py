#Importin library to use random numbers
from random import randint 

#Rival's pokemon Health Points
rival_maxhp = 80
rival_hp =  80

#My pokemon's Health Points
my_maxhp = 90
my_hp = 90


#Function to obtain the percentage
#y = the number that is the 100%
#z = the number you want to know what percentage is
def calc_percentage(y: float, z: float):
    return (y*100/z)

#This function draws the pokemon hp in a bar that looks like this [#####     ]
def draw_hp(max_hp: float, hp: float):
    hp_graph = "["
    hp_percent = calc_percentage(hp, max_hp)
    for x in range (0, 100, 10):
        if x < hp_percent:
            hp_graph += "#"
        else:
            hp_graph += " "
    hp_graph += "]"
    print(hp_graph)    

#Battle cycle
while rival_hp > 0 and my_hp > 0:
    #Pokemons life
    print("\n\nRival's pikachu life is: {}".format(rival_hp))
    draw_hp(rival_maxhp, rival_hp)
    print("your squirtle's life is {}".format(my_hp))
    draw_hp(my_maxhp, my_hp)
    #Rival's turn
    print("\nYour rival's turn")
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
    print("\nIt's your turn wich attack do you want to use?:")
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
                    print("Squirtle uses Tackle -10")
                    rival_hp -= 10
                case 1:
                    print("Squirtle uses Water gun -15")
                    rival_hp -= 15
                case 2:
                    print("Squirtle uses Bubble -20")
                    rival_hp -= 20
                #Check if the attack selected is a valid option
                case _:
                    print("Error: select a number between 0-2")
    input("Press enter to continue...")

#End of the combat
print("\n\nRival's pikachu life is: {}".format(rival_hp))
draw_hp(rival_maxhp, rival_hp)
print("your squirtle's life is {}".format(my_hp))
draw_hp(my_maxhp, my_hp)
if rival_hp <= 0:
    print("Rival's pikachu has fainted, you win !")
else:
    print("Your squirtle has fainted. Going to a pokemon center")