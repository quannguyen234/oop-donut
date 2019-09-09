#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 17:18:44 2019

@author: quannguyen
"""

from dough import Dough
from person import Person
from filling import Filling
from glaze import Glaze

def ultimate_donut(style, sweetness, fatness):
    
    for filling in all_fillings:
        if filling.style == style and sweetness == filling.sweetness and filling.fatness ==  fatness:
            print(f'Your donut filling is {filling.name}')
            
    for glze in all_glazes:
        if glze.sweetness == sweetness and glze.fatness == fatness:
            print(f'Your donut glaze is {glze.name}')
            
    
        
        
    
#style: Classic
#0
mint = Filling("Mint", "Classic", 0, 0)
coffee = Filling("Coffee", "Classic", 0, 1)
#1   
vanilla = Filling("Vanilla", "Classic", 1, 1)
chocolate = Filling("Chocolate", "Classic", 1, 2)
#2
cookies_n_cream = Filling("Cookies and Cream", "Classic", 2, 1)
caramel = Filling("Caramel", "Classic", 2, 2)


#style: Fruity
#0
lemon = Filling("Lemon", "Fruity", 0, 0)
passionfruit = Filling("Passion Fruit", "Fruity", 0, 1)
#1
apple = Filling("Apple", "Fruity", 1, 1)
coconut = Filling("Coconut", "Fruity", 1, 2)
#2
strawberry = Filling("Strawberry", "Fruity", 2, 1)
banana = Filling("Banana", "Fruity", 2, 2)

#style: Explorer
#0
matcha = Filling("Matcha", "Explorer", 0, 0)  
pistachio = Filling("Pistachio", "Explorer", 0, 1)
#1
milk_tea = Filling("Milk Tea", "Explorer", 1, 1)
almond_cream = Filling("Almond Cream", "Explorer", 1, 2)

#2
honey_lavender = Filling("Honey Lavender", "Explorer", 2, 1)
nuttella = Filling("Nutella", "Explorer", 2, 2)

all_fillings = [mint, coffee, vanilla, chocolate, caramel, passionfruit, lemon, coconut, apple, strawberry,matcha, pistachio,milk_tea,almond_cream, nuttella, honey_lavender]
#0
no_glaze =  Glaze("No Glaze", 0, 0)
powder_sugar = Glaze("Powder Sugar", 0, 1)

cinnamon_sugar = Glaze("Cinnamon Sugar", 1, 1)
chocolate_glaze = Glaze("Chocolate Glaze", 1, 2)
#2
sugar = Glaze("Sugar Glaze", 2, 1)
sprinkles = Glaze("Sprinkles", 2, 2)

all_glazes = [no_glaze, cinnamon_sugar, chocolate_glaze, sugar, sprinkles]
#0
#yeast = Dough("Yeast")
#1
##quan = Person("Quan", False)


