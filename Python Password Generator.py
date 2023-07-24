#!/usr/bin/env python
# coding: utf-8

# In[7]:


# necessary imports
import secrets
import string

# define the alphabet
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

# ask user for desired password length
pwd_length = int(input('How many characters do you want your password to be?'))

# generate password meeting constraints. password must contain atleast 2 numbers and 2 special characters.
while True:
  pwd = ''
  for i in range(pwd_length):
    pwd += ''.join(secrets.choice(alphabet))

  if (any(char in special_chars for char in pwd) and 
      sum(char in digits for char in pwd)>=2):
          break
print(pwd)


# In[ ]:




