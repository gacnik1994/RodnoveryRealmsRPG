# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 10:38:19 2024

@author: alesgacnik
"""

class Menus:
    
    def Menus(self):
        self.name = "menus"
    
    def print_main_menu(self):
        print(" --------------------------------- ")
        print("|   ***  RODNOVERY REALMS  ***    |")
        print(" --------------------------------- ")
        print("| Welcome to game Rodnover realms |")
        print("| Type START to start the game    |")
        print("| Type EXIT to close the game     |")
        print(" ================================= ")
        
    def print_game_start(self):
        print(" --------------------------------- ")
        print("|   ***  Starting the game  ***   |")
        print(" --------------------------------- ")
        print("| Please type the game you would  |")
        print("| like to start.                  |")
        print("| Type NEW to start a new game    |")
        print("| Type LOAD to load a saved game  |")
        print(" ================================= ")
        
    def print_char_class(self):
        print(" --------------------------------- ")
        print("|    Chose your character class   |")
        print(" --------------------------------- ")
        print("| Please type the class that you  |")
        print("| would like to play with your    |")
        print("| character.                      |")
        print("| Type WARRIOR for warrior class  |")
        print("| Type MAGE for mage class        |")
        print(" ================================= ")
        
    def print_type_char_name(self):
        print(" --------------------------------- ")
        print("| Please type the name of your    |")
        print("| character.                      |")
        print(" ================================= ")
        
    def print_sword(self):
        print(" --------------------------------- ")
        print("|               /\                |") 
        print("|               ||                |") 
        print("|               ||                |") 
        print("|               ||                |") 
        print("|               ||                |") 
        print("|               ||                |") 
        print("|            [==[]==]             |") 
        print("|               ||                |") 
        print("|               []                |") 
        print(" --------------------------------- ")
        
    def print_shield(self):
        print(" --------------------------------- ")
        print("|             ------              |") 
        print("|           /   ||   \            |") 
        print("|         |     --     |          |") 
        print("|        |     /**\     |         |") 
        print("|       |=====|****|=====|        |") 
        print("|        |     \**/     |         |") 
        print("|         |     --     |          |") 
        print("|           \   ||   /            |") 
        print("|             ------              |") 
        print(" --------------------------------- ")
        
    def print_wellcome(self):
        print(" --------------------------------- ")
        print("| Wellcome to the demo of RPG     |")
        print("| Rodnovery realms. In this demo  |")
        print("| we will test battle mechanic    |")
        print("| of the game. Let's hope         |")
        print("| everything works. :)            |")
        print(" --------------------------------- ")
        
    def print_start_battle(self):
        print(" --------------------------------- ")
        print("| Type START to start the battle  |")
        print("| Type END to close the game      |")
        print(" --------------------------------- ")
        
    def print_battle_instructions(self):
        print(" --------------------------------- ")
        print("| Type the number next to the     |")
        print("| abiliti that you want to use.   |")
        print(" --------------------------------- ")
        
    def print_battle_stance(self, atacking, defending):
        print(" --------------------------------- ")
        print("| " + atacking + " is attacking.")
        print("| " + defending + " is defending.")
        print(" --------------------------------- ")
        
        
    def print_atacking(self, ability):
        print(" --------------------------------- ")
        print("| Type 1 to use basic attack")
        print("| Type 2 to use " + ability)
        print(" --------------------------------- ")
        
    def print_defending(self):
        print(" --------------------------------- ")
        print("| Type 1 to block")
        print("| Type 2 to dodge")
        print(" --------------------------------- ")