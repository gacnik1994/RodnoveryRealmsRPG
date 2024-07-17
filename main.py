# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:15:51 2024

@author: alesgacnik
"""

import character
from os import system, name
from time import sleep
import sys
from MainMenu import Menus
import random
import pygame


counter = 0
starting = True 
while(starting): 
       
    if counter == 0:
        menus = Menus()
        menus.print_main_menu()
        counter = counter + 1  
    enter = input("->")
    enter = enter.upper()
    
    if enter == "START":
        counter = 0
        starting = False
        
        menus.print_game_start()
        start_game = input("->")
        start_game = start_game.upper()
        
        if start_game == "NEW":
            main_character = character.Character()
            menus.print_char_class()
            chose_class = input("->")
            chose_class = chose_class.upper()
            
            if chose_class == "WARRIOR" or chose_class == "MAGE":
                 menus.print_type_char_name()
                 character_name = input("->")
                 main_character.character(character_name, chose_class)
                 main_character.print_character()
                 sleep(5)
                 menus.print_wellcome()
                 sleep(5)
                 bad_guy = character.Character()
                 if chose_class == "MAGE":
                     bad_guy.character("Thief", "WARRIOR")
                 elif chose_class == "WARRIOR":
                     bad_guy.character("Evil wizard", "MAGE")
                 menus.print_start_battle()   
                 starting_battle = input("->")
                 
                 starting_battle = starting_battle.upper()
                 if starting_battle == "START":
                    menus.print_battle_instructions()
                    mc_attacking =  True
                    list1 = [1,2]
                    while bad_guy.get_hp() > 0 and main_character.get_hp() > 0:
                        if mc_attacking:
                            menus.print_battle_stance(main_character.get_name(), bad_guy.get_name())
                            menus.print_atacking(main_character.get_skill().get_name())
                            attack = input("->")
                            mc_attacking = False
                            if attack == "1":
                                response = random.choice(list1)
                                print("| " + main_character.get_name() + " used normal attack.")
                                sleep(1)
                                if response == 1:
                                    if (main_character.get_attack() + main_character.get_items().get_attack()) > bad_guy.get_defense():
                                        new_hp = bad_guy.get_hp() + bad_guy.get_defense() - main_character.get_attack() - main_character.get_items().get_attack()
                                        bad_guy.set_hp(new_hp)
                                        print(bad_guy.get_hp())
                                        sleep(1)
                                    else:
                                        print("| " + bad_guy.get_name() + " blocked the attack.")
                                elif response == 2:
                                    if main_character.get_speed() > bad_guy.get_speed():
                                        new_hp = bad_guy.get_hp() + bad_guy.get_defense() - main_character.get_attack() - main_character.get_items().get_attack()
                                        bad_guy.set_hp(new_hp)
                                        print(bad_guy.get_hp())
                                        sleep(1)
                                    else:
                                        print("| " + bad_guy.get_name() + " dodged the attack.")
                            elif attack == "2":  
                                print("| " + main_character.get_name() + " used " + main_character.get_skill().get_name() + ".")
                                sleep(1)
                                response = random.choice(list1)
                                if response == 1:
                                    if (main_character.get_skill().get_attack()+main_character.get_attack()) > bad_guy.get_defense():
                                        new_hp = bad_guy.get_hp() + bad_guy.get_defense() - main_character.get_skill().get_attack() - main_character.get_items().get_attack()
                                        bad_guy.set_hp(new_hp)
                                        print(bad_guy.get_hp())
                                        sleep(1)
                                    else:
                                        print("| " + bad_guy.get_name() + " blocked the attack.")
                                elif response == 2:
                                    if (main_character.get_skill().get_speed()+main_character.get_speed()) > bad_guy.get_speed():
                                        new_hp = bad_guy.get_hp() + bad_guy.get_defense() - main_character.get_skill().get_attack() - main_character.get_items().get_attack()
                                        bad_guy.set_hp(new_hp)
                                        print(bad_guy.get_hp())
                                        sleep(1)
                                    else:
                                        print("| " + bad_guy.get_name() + " dodged the attack.")
                        else:
                            mc_attacking = True
                            menus.print_battle_stance(bad_guy.get_name(), main_character.get_name())
                            menus.print_defending()
                            defend = input("->")
                            response = random.choice(list1)
                            if response == 1:
                                print("| " + bad_guy.get_name() + " used normal attack.")
                                sleep(1)
                                if defend == "1":
                                    if (bad_guy.get_attack() + bad_guy.get_items().get_attack()) > main_character.get_defense():
                                        mc_hp = main_character.get_hp()
                                        new_hp = main_character.get_hp() + main_character.get_defense() - (bad_guy.get_attack() + bad_guy.get_items().get_attack())
                                        main_character.set_hp(new_hp)
                                        print("You lost " + str(mc_hp-new_hp) + " HP.")
                                        print("Your new HP is " + str(new_hp))
                                        sleep(1)
                                    else:
                                        print("| You blocked the attack.")
                                        sleep(1)
                        
                                elif defend == "2":
                                    if main_character.get_speed() < bad_guy.get_speed():
                                        mc_hp = main_character.get_hp()
                                        new_hp = main_character.get_hp() + main_character.get_defense() - (bad_guy.get_attack() + bad_guy.get_items().get_attack())
                                        main_character.set_hp(new_hp)
                                        print("You lost " + str(mc_hp-new_hp) + " HP.")
                                        print("Your new HP is " + str(new_hp))
                                        sleep(1)
                                    else:
                                        print("| You dodged the attack.")
                                        sleep(1)
                        
                            elif response == 2:   
                                print("| " + bad_guy.get_name() + " used " + bad_guy.get_skill().get_name() + ".")
                                sleep(1)
                                response = random.choice(list1)
                                if defend == "1":
                                    if (bad_guy.get_skill().get_attack()+bad_guy.get_attack()) > main_character.get_defense():
                                        mc_hp = main_character.get_hp()
                                        new_hp = main_character.get_hp() + main_character.get_defense() - (bad_guy.get_skill().get_attack()+bad_guy.get_attack())
                                        main_character.set_hp(new_hp)
                                        print("You lost " + str(mc_hp-new_hp) + " HP.")
                                        print("Your new HP is " + str(new_hp))
                                        sleep(1)
                                    else:
                                        print("| You blocked the attack.")
                                        sleep(1)
                        
                                elif defend == "2":
                                    if (bad_guy.get_skill().get_speed()+bad_guy.get_speed()) > main_character.get_speed():
                                        mc_hp = main_character.get_hp()
                                        new_hp = main_character.get_hp() + main_character.get_defense() - (bad_guy.get_skill().get_attack()+bad_guy.get_attack())
                                        main_character.set_hp(new_hp)
                                        print("You lost " + str(mc_hp-new_hp) + " HP.")
                                        print("Your new HP is " + str(new_hp))
                                        sleep(1)
                                    else:
                                        print("| You dodged the attack.")
                                        sleep(1)
                        if main_character.get_hp() <= 0:
                            print("You lost the battle.")
                        elif bad_guy.get_hp() <= 0:
                            print("You won the battle.")
                        
                 elif starting_battle == "END":
                     sys.exit()
                 
                 
        elif start_game == "LOAD":
           print("Game saving and loading not supported at the moment") 
        else:
            print("Wrong input, please try again!")
        
        
    elif enter == "EXIT":
        sys.exit()
    else:
        if counter < 6:
            print("Please type START or EXIT \n")
            sleep(2)
        else:
            print("Too many false inputs, the game will close!")
            sleep(2)
            sys.exit()





