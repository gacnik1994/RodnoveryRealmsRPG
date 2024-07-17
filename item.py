# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:52:30 2024

@author: alesgacnik
"""

class Item(object):
    
    def item(self, name):
        if name == "Sword":
            self.name = name
            self.attack = 50
            self.defense = 10
            self.weight = 20
        elif name == "Shield":
            self.name = name
            self.attack = 10
            self.defense = 50
            self.weight = 10
        elif name == "Dagger":
            self.name = name
            self.attack = 30
            self.defense = 0
            self.weight = 0
        elif name == "Staff":
            self.name = name
            self.attack = 10
            self.defense = 40
            self.weight = 30
        elif name == "greatsword":
            self.name = name
            self.attack = 80
            self.defense = 0
            self.weight = 70
            
    def print_out_item(self):
        
        print("| Name of the item: " + self.name)
        print("| ATK of the item: " + str(self.attack))
        print("| DEF of the item: " + str(self.defense))
        print("| WGT of the item:" + str(self.weight))
        print(" --------------------------------- ")
        
    def get_attack(self):
        return self.attack
    
    def get_defense(self):
        return self.defense
    
    def get_weight(self):
        return self.weight