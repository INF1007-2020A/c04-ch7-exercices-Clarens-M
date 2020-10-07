#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import Turtle
import math
from exercices import frequence

# TODO: Définissez vos fonction ici

def volMas(a, b, c, mv):
    v = (4/3) * math.pi * a * b * c
    
    m = mv * v
    return m, v

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(volMas(3, 4, 5, 78))
    (lambda sentence: sorted(frequence(sentence), key = frequence(sentence).__getitem__)[-1])("il s'agit d'une phraaaaaaaaaaaaaaaaaaaaaaaaaaaaaase")
    
    pass
