#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import Turtle
import math
from exercices import frequence

# TODO: Définissez vos fonction ici

#def volMas(a, b, c, mv):
 #   v = (4/3) * math.pi * a * b * c
 #   
 #   m = mv * v
 #   return m, v

def branche(alpha, longueur):
    if longueur > 0:
        setheading(alpha)
        forward(longueur)
        branche1 = pos()
        backward(longueur)
        setheading(alpha/2)
        forward(longueur)
        branche2 = pos()
        penup() 

def dessin():
    penup()
    color("green")
    pensize(10)
    setx(0)
    sety(0)
    setheading(90)
    pendown()
    forward(100)
    alpha = 60
    for i in range(0, 5):
        for i in range

    pendup()
    done()  
        
if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
 #   print(volMas(3, 4, 5, 78))
 #   (lambda sentence: sorted(frequence(sentence), key = frequence(sentence).__getitem__)[-1])("il s'agit d'une phraaaaaaaaaaaaaaaaaaaaaaaaaaaaaase")
    
    pass
