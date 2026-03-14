# 1. Write a python program to display a user entered name followed by Good 
# Afternoon using input () function. 







# 2. Write a program to fill in a letter template given below with name and date. 
# letter = '''  
#        Dear <|Name|>, 
#        You are selected! 
#        <|Date|> 
#         ''' 
 
letter = '''  
       Dear <|Name|>, 
       You are selected! 
       <|Date|> 
        ''' 
print(letter.replace("<|Name|>"  , "pawan").replace("<|Date|> " , "17 Dec 2027"))



# 3. Write a program to detect double space in a string.  

name = "pawan mali  uniyara"      

print(name.find("  "))


# 4. Replace the double space from problem 3 with single spaces. 


name = "pawan mali  uniyara"      

print(name.replace("  " , " "))

# Strings are immutable which means that you cannot change them by running functions on them



# 5. Write a program to format the following letter using escape sequence 
# characters. 
# letter = "Dear Harry, this python course is nice. Thanks!"

letter = "Dear sir,\n\t this python course is nice.\n Thanks!"

print(letter)