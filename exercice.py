#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici
#import "./recette.py"


# TODO: Définissez vos fonction ici
def comparateur_de_file(file1, file2):
    with open(file1, "r") as f1, open(file2, "r") as f2 :
        for line in file1:
            if line != file2.readline():
                print("erreur")

def triple_space(file, file1):
    with open(file, encoding="utf-8") as f1, open(file1, "w", encoding="utf-8") as f2:
        for line in f1:
            f2.write(line.replace(" ", "   "))




if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    triple_space("./exemple.txt", "./exemple_triple.txt")
    pass
