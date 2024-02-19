import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

total = lower + upper + digits + symbols
print("Welcome To Random Password Generator!!!\n")

def my_password():
    length = int(input("Enter The Length Of The Password: "))
    password = random.sample(total, length)
    new_pass = "".join(password)
    print(new_pass)
    choice = input("Do You Want To Continue?Y/N: ")
    if choice=="Y" :
        my_password()
    else:
        exit    
my_password()
