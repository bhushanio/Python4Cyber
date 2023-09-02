#Strong Random Password Generator

#Libraries
import random
import string

#Function
def ran_pass(length):
    character = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(character) for _ in range(length))
    return password

#Test Code

#password = ran_pass(12) --static code
#password = ran_pass(int(input("Enter length of password: "))) --dynamic code

#print(f'Password : {password}')  -- output for static and dynamic code

print("Password is : ", ran_pass(int(input("Enter length of password: ")))) --complex code

#Note: This program ask user to input length of password and it generates random hardcoded password
