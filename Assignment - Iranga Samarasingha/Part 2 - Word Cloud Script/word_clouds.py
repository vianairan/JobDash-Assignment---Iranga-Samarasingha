# -*- coding: utf-8 -*-
"""
Date: Jan 23rd, 2015 
@author: Iranga Samarasingha
Purpose: Assignment for JobDash
Question: Write a stand alone Python script that creates word clouds.To do this, you'll first need to build the data. Write code that takes a long string and builds its word cloud data in a dictionary, where the keys are the words and the values are the number of times the words occured.

"""

# Import Libraries
import string
from pprint import pprint

# Input text to test the script
original_string = "Write a stand alone Python script that creates word clouds. To do this, you'll first need to build the data. Write code that takes a long string and builds its word cloud data in a dictionary, where the keys are the words and the values are the number of times the words occured.";

def exclude_punctuation( input_str ):
    """
     Purpose: Excludes all the punctuation marks conatained in a string and ...
              returns a new string without any punctuation marks.
              
     Input Args: 
         input_str - String that needs to be processed (Type: String) 
     
     Returns: 
         output_str - String with out punctuation marks (Type: String) 
         
     Usage: 
         output_str = exclude_punctuation(input_str)
     
     """
    output_str = ""; # Initialize string variable for output string
    
    for char in input_str:      # Ite a = dictrate through each charactor of the string
       if char not in string.punctuation: # Add the charactor to the output if not included in the standard string of punctuations
           output_str = output_str + char
    
    return output_str  # Returns the output string 
    
 
def count_words( input_list ):
    """
     Purpose: Counts the number of occurances of each string in the input list and ...
              returns a dictionary with words and the frequency.
              
     Input Args:
         input_list - List of strings (Type: List)
          
     Returns: 
         word_dict - Dictionary of words and frequency (Type: Dictionary)
         
     Usage: output_dict = count_words(input_list)
     
     """

    word_dict = {}; # Initialize a dictionary (hashtable) to store the words and frequency
    
    for value in input_list:  # Iterate through each word in the list
        if value not in word_dict:
            word_dict[value] = 1   
        else:
            word_dict[value] += 1
    
    return word_dict  # Returns the output dictionary 

print "START"
print "-----"
print "Original Input String : "
print "....................."
print ""
print original_string   
print ""
print ""
   
new_string = exclude_punctuation(original_string)

word_list = new_string.lower().split();

new_dict = count_words(word_list)

print "Result : "  
print "......."
print ""  
pprint(new_dict)
print ""
print ""
print "END"
print "---"