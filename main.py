#Importin library to use random numbers
from random import randint 
from subprocess import run as sprun


#Rival's pokemon Health Points
RIVAL_MAXHP = 80

#My pokemon's Health Points
MY_MAXHP = 90


#Function to obtain the percentage
#y = the number that is the 100%
#z = the number you want to know what percentage is
def calc_percentage(y: float, z: float):
    return (y*100/z)

#This function draws the pokemon hp in a bar that looks like this [#####     ]
def draw_hp(max_hp: float, hp: float):
    hp_percent = calc_percentage(hp, max_hp)
    hp_graph = "[" + "#"*(int(hp_percent/10)) +  " "*(int(10-(hp_percent/10))) +"]"
    print(hp_graph)    


def draw_pokemons_hp (rival_hp, my_hp):
    print("\n")
    if rival_hp < 0:
        rival_hp = 0
    if my_hp < 0:
        my_hp = 0
    print("Rival's pikachu life is: {}".format(rival_hp))
    draw_hp(RIVAL_MAXHP, rival_hp)
    print("your squirtle's life is {}".format(my_hp))
    draw_hp(MY_MAXHP, my_hp)
    print("\n")
    
#Battle cycle
def battle_cycle():
    
    #Actual hp from the pokemons
    rival_hp =  RIVAL_MAXHP
    my_hp = MY_MAXHP   
    while rival_hp > 0 and my_hp > 0:
        #Clear screen
        sprun("clear", shell=True)
        #Pokemons life
        draw_pokemons_hp(rival_hp, my_hp)
        input("Press enter to continue...")
        sprun("clear", shell=True)
        #Rival's turn
        print("Your rival's turn")
        input("Press enter to continue...")
        sprun("clear", shell=True)
        rival_atk = randint(0, 1)
        #If the rival attack is 0 then uses electro ball otherwise uses thunder wave
        if(rival_atk == 0):
            print("Pikachu uses Electro Ball -20")
            my_hp -= 20
        else:
            print("Pikachu uses Thunder Wave -10")
            my_hp -= 10
        draw_pokemons_hp(rival_hp, my_hp)
        input("Press enter to continue...")
        if my_hp <= 0:
            break
        sprun("clear", shell=True)
        draw_pokemons_hp(rival_hp, my_hp)
        #Your turn
        print("It's your turn wich attack do you want to use?:")
        print("0. Tackle -- atk 10")
        print("1. Water gun -- atk 15")
        print("2. Bubble -- atk 20")
        print("3. Splash -- does nothing")
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
                    case 3:
                        print("Squirtle uses Splash -0")
                    #Check if the attack selected is a valid option
                    case _:
                        print("Error: select a number between 0-2")
        input("Press enter to continue...")
        sprun("clear", shell=True)

    #End of the combat
    draw_pokemons_hp(rival_hp, my_hp)
    if rival_hp <= 0:
        print("Rival's pikachu has fainted, you win !")
    else:
        print("Your squirtle has fainted. Going to a pokemon center")

battle_cycle()