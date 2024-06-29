'''
Q1. In DevOps, security is a crucial aspect, and ensuring strong passwords is essential. Create a Python script to check the password strength. 

●       Implement a Python function called check_password_strength that takes a password string as input.

●       The function should check the password against the following criteria:

    ○       Minimum length: The password should be at least 8 characters long.

    ○       Contains both uppercase and lowercase letters.

    ○       Contains at least one digit (0-9).

    ○       Contains at least one special character (e.g., !, @, #, $, %).

●       The function should return a boolean value indicating whether the password meets the criteria.

●       Write a script that takes user input for a password and calls the check_password_strength function to validate it.

●       Provide appropriate feedback to the user based on the strength of the password.  
'''
import re
def check_password_strength(strPass):
    #using the regualr expression to check the validity.
    #[a-z] to check of password contains lowercase letter
    #[A-Z] to check of password contains uppercase letter
    #[0-9] to check of password contains numric chacters
    # and last expression is to check for special characters
    #.{8,} is for minimun length of pass

    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$%^&+=]).{8,}"
    #using the match fucntion to check if Password is strong or not
    match = re.match(pattern, strPass)
    if(bool(match)):
        print("it's a valid Password")
    else:
        print("In valid Password\nPassword should \nMinimum length: The password should be at least 8 characters long.\nContains both uppercase and lowercase letters.\nContains at least one digit (0-9).\nontains at least one special character (e.g., !, @, #, $, %). ")


strPass = input("Enter the Password\n ")
check_password_strength(strPass)
