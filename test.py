#!/usr/bin/python

import sys
import os

class Test:        # define parent class 
    
    def helloWorld(self):
        print 'Hello World ...'
    
    def listMethods(self):
        print Test.__dict__.keys()
        
    def writeFile(self):
        print 'Calling writeFile method from class ' + sys.argv[0]
        file_name =  raw_input("enter new filename: ") 
        try:
            file = open(file_name, "w")
            file_text = raw_input("Enter text: ")   
            file.write(file_text)
            file.write("\n")
            file.close()
        except IOError:
            print "There was an error writing to", file_name
            sys.exit()

            
         
p = Test()          # instance of class
print 'List of methods from class ' + p.__class__.__name__
p.listMethods()     # list all methods in the class  


method_to_run = raw_input("Enter method to run: ") 
#_member = getattr(p, sys.argv[1])
_member = getattr(p, method_to_run) 
_member()  