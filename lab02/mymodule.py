# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 09:09:43 2023

@author: mnaee
"""

# Define some variables:
ageofqueen = 78
# define some functions
def printhello():
    print ("hello")

# define a class
class Piano:
    def init (self):
        self.type = input("What type of piano?: ")
        self.height = input("What height (in feet)?: ")
        self.price = input("How much did it cost?: ")
        self.age = input("How old is it (in years)?: ")

    def printdetails(self):
        print ("This piano is a/an " + self.height + " foot")
        print (self.type, "piano, " + self.age, "years old and costing " +
               self.price + " dollars.")