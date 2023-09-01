#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello")


# In[23]:


## INPUTS FROM USERS 

num1 = int(input ("what is the first number ?"))
num2 = int (input ("what is the fsecond number ?"))


# FUNCTIONS 

def add (n1 , n2):
        return n1 + n2
    
def substract (n1 , n2):
        return n1 - n2
    
def divider (n1 , n2):
        return n1 / n2
    
def multiply (n1 , n2):
        return n1 * n2
    

# OPREATION OBJECTS
opereations = {
    "+": add,
    "-": substract,
    "/": divider,
    "*": multiply

}

#LOOP THROUGHT AND DISPLAY SYMBOL

for symbol in opereations :
     print(symbol)
        
opereations_symbol = input("pik an opreation from the line above")
calculation_function= opereations[opereations_symbol]
         
print (opereations_symbol)

answer= calculation_function(num1 , num2)
print(answer)


# In[ ]:





# In[ ]:




