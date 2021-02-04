from exercices.exercice1 import *

def test_recherche_non_vide():
    assert recherche(3, [3, 2, 1, 3, 2, 1]) == [0, 3] 

def test_recherche_vide():
    assert recherche(4, [1, 2, 3]) == [] 