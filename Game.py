#!/usr/bin/env python

import random

def main():
    
    #Prepare the elements and clues list
    ElemenLists=[
        "Hydrogen",
        "Helium",
        "Lithium",
        "Carbon",
        "Nitrogen",
        "Oxygen",
        "Fluorine",
        "Neon",
        "Aluminium",
        "Silicon",
        "Sulfur",
        "Chlorine",
        "Krypton"
    ]
    clue1=[
        "Water Constituem",
        "Balloon",
        "Battery",
        "The most organic compound", # test update sync
        "Most needed by plant",
        "Most needed by human",
        "toothpaste",
        "To protect bulb elemen from burn",
        "Conduct heat efficiently",
        "Glass",
        "firecrackers",
        "we drink in tap water",
        "feared superman"
    ]
     
    
    #The game start with 3 chances to guess the element
    while True:

        #Initialise the variables
        Ind=random.randint(0,12)
        guess="None"
        count=3

        while ElemenLists[Ind].lower()!=guess.lower() and count>0:
            guess=input("Guess what is the name of periodic element I'm thinking of? ")
            if ElemenLists[Ind].lower()==guess.lower():
                if count==3:
                    print("Do you read my mind???....Bravo you are superb")
                else:
                    print("You are genius!")
            else:
                count-=1 #Reduce the chances
                print("Try again, you have ",count," Chance(s)\n")
                print("Here some clues: ",clue1[Ind])
        if count<=0:
            cont=input("Oh no...Want to try again? Y/N ")
        else:
            cont=input("Guess more? Y/N ")
        if cont.capitalize()=="N":
            print("THANKS FOR TESTING MY GAME")
            break 
    
main()
