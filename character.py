# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:16:30 2024

@author: alesgacnik
"""
from item import Item
from abilities import Abilities

class Character(object):
    #condition = "New"
    
    def character(self, name, char_class,):
        self.name = name
        
        if char_class == "WARRIOR":
            self.char_class = "Warrior"
            self.hit_points = 100
            self.attack = 50
            self.defense = 50
            self.mana = 0
            self.speed = 50
            self.strength = 50
            self.stamina = 50
            self.items = Item()
            self.items.item("Sword")
            self.skill_list = Abilities()
            self.skill_list.abi("strike")
            
        elif char_class == "MAGE":
            self.char_class = "Mage"
            self.hit_points = 100
            self.attack = 20
            self.defense = 10
            self.mana = 100
            self.speed = 40
            self.strength = 30
            self.stamina = 30
            self.items = Item()
            self.items.item("Staff")
            self.skill_list = Abilities()
            self.skill_list.abi("fireball")
        
    def get_name(self):
        return self.name
      
    def get_hp(self):
        return self.hit_points
    
    def get_attack(self):
        return self.attack
    
    def get_defense(self):
        return self.defense
    
    def get_mana(self):
        return self.mana
    
    def get_speed(self):
        return self.speed
        
    def get_strength(self):
        return self.strength
    
    def get_stamina(self):
        return self.stamina
    
    def get_items(self):
        return self.items
    
    def get_skill(self):
        return self.skill_list
    
    
    def set_name(self, name):
        self.name = name
        
    def set_hp(self, hit_points):
        self.hit_points = hit_points
    
    def set_attack(self, attack):
        self.attack = attack
    
    def set_defense(self, defense):
        self.defense = defense
    
    def set_mana(self, mana):
        self.mana = mana
    
    def set_speed(self, speed):
        self.speed = speed
        
    def set_strength(self, strength):
        self.strength = strength
    
    def set_stamina(self, stamina):
        self.stamina = stamina
    
    def set_items(self, items):
        self.items = items
    
    def set_skill(self, skill_list):
        self.skill_list = skill_list
        
    def print_character(self):
        print(" --------------------------------- ")
        print("| ***  Character information  *** |")
        print(" --------------------------------- ")
        print("| Character name: " + self.name)
        print("| Class: " + self.char_class)
        print("| HP: " + str(self.hit_points))
        print("| ATK: " + str(self.attack))
        print("| DEF: " + str(self.defense))
        print("| MANA: " + str(self.mana))
        print("| SPD: " + str(self.speed))
        print("| STR: " + str(self.strength))
        print("| STM: " + str(self.stamina))
        print(" --------------------------------- ")
        print("|       **  Equipement  **        |")
        print(" --------------------------------- ")
        self.items.print_out_item()
        print(" --------------------------------- ")
        print("|       **  Abilities   **        |")
        print(" --------------------------------- ")
        self.skill_list.print_out_abi()