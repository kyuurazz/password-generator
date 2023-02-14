import random
import string
import os

os.system('cls')
print('PYTHON PASSWORD GENERATOR')
print('=========================')

# input the length of password
length = int(input('Enter the length of password: '))

# define data 
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

# combine the data 
combine = lower + upper + num + symbols
temp = random.sample(combine, length)
password = "".join(temp)

# output
print("Result:", password +"\n")
