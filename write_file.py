#!/usr/bin/env python
# encoding: utf-8
"""
write_file.py

Created by David Araujo on 2013-03-04.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import unittest


class write_file:
    def __init__(self):
        self.file_name = "david.txt"
       
    def start_writing(self):
         try:
           # open file stream    
           file_name = 'david.txt'
           file = open(file_name, "w")
         except IOError:
           print "There was an error writing to", file_name
           sys.exit()
         print "Enter '", file_finish,
         print "' When finished"
         while file_text != file_finish:
           file_text = raw_input("Enter text: ")
           if file_text == file_finish:
             # close the file
             file.close
             break
           file.write(file_text)
           file.write("\n")
         file.close()
         file_name = raw_input("Enter filename: ")
         if len(file_name) == 0:
           print "Next time please enter something"
           sys.exit()
         try:
           file = open(file_name, "r")
         except IOError:
           print "There was an error reading file"
           sys.exit()
         file_text = file.read()
         file.close()
         print file_text     


#w = write_file()
#w.start_writing()

#class write_fileTests(unittest.TestCase):
#    def setUp(self):
#        write_file
#    def write_file():    
        
#if __name__ == '__main__':
#    unittest.main()             
    
    
    
    

    