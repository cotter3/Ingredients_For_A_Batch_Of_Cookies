# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 18:48:39 2018

@author: Chris Otter
"""

#1.5 cups sugar, 1 cup of butter, 2.75 flour: 48 cookies 

import pymsgbox

#variables for amount of each ingredient
s = 0.03125 #sugar
b = 0.02083333333333333333333333333333 #butter
f = 0.05729166666666666666666666666667 #flour

#calculate function
def calculate():
        # asks the user to input the amount cookies
        amount = float(pymsgbox.prompt('How many cookies would you like to make?', 'Cookies Calc'))
        totalf = float(f * amount)
        totalb = float(b * amount)
        totals = float(s * amount)
        #displays the amount of each ingredient
        pymsgbox.alert("The amount of cups per ingredient are: " + "Flour: " + str(totalf) + " Butter: " + str(totalb) + " Sugar: " + str(totals))
        "OK"
        return again()

#loop function
def again():
    while True:
        #asks to make another batch
        again = pymsgbox.confirm('Would you like to check another batch of cookies?', 'More Cookies', ["Yes", 'No'])
        if again not in {"Yes","No"}:
            print("please enter valid input")               
        elif again == "No":
            return pymsgbox.alert("Thank you for using my Cookie calculator!")
        elif again == "Yes":
            # call function to start the calc again
            return calculate()
calculate()




