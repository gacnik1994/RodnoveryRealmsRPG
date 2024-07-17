# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 14:22:22 2024

@author: alesgacnik
"""

class Abilities(object):
    
    def abi(self, name):
        if name == "fireball":
            self.name = name
            self.attack = 120
            self.mana = 10
            self.speed = 30
        elif name == "strike":
            self.name = name
            self.attack = 30
            self.mana = 0
            self.speed = 10
        
    def print_out_abi(self):
        print("| " + self.name + " -- ATK: " + str(self.attack) + " MANA: " + str(self.mana) + " SPD: " + str(self.speed))
        print(" --------------------------------- \n")
        
    def get_name(self):
        return self.name
    
    def get_attack(self):
        return self.attack
    
    def get_mana(self):
        return self.mana
    
    def get_speed(self):
        return self.speed