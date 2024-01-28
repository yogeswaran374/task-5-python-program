"""write a python function to validate the regular expression of the following

a. email address
b. mobile nunber of bangladesh
c. telephone number of usa
d. 16 character of password"""


import re

def validate_email_address(email_id):
    pattern = "^[a-z0-9]{13}+@+[gmail]+.+com$"
    email = re.match(pattern, email_id)
    if email:
        return "Entered email id is valid"
    else:
        return "Entered email id is invalid"
    
"""
1. country code is +880
2. it contains 11 digits
3. number starts from 0 or 1

"""    
def validate_mobile_number_of_bangladesh(mobile_number):
    pattern = "^[+][8][8][0][ ]+[01]{2}[0-9]{9}$"
    mobile_number = re.match(pattern, mobile_number)
    if mobile_number:
        return "Entered mobile number is valid"
    else:
        return "Entered mobile number is invalid"


"""
1. country code '+1'
2. it contains 3 digit of area code
3. then the phone number is 7 digit
"""


def validate_telephone_number_of_USA(Telephone_number):
    pattern = "^[+][1][1-9]{3}[0-9]{7}$"
    Telephone_number = re.match(pattern, Telephone_number)
    if Telephone_number:
        return "Entered telephone number is valid"
    else:
        return "Entered telephone number is invalid"

"""
1. 16 digit alpha-numeric password
2. it contains alphabets of uppercae, lower case special characters and numbers
"""


def validate_password(password):
    pattern = "^[A-Za-z0-9!@#$%^&*-+=_()]{16}$"
    password = re.match(pattern, password)
    if password:
        return "Entered password is valid"
    else:
        return "Entered password is invalid"


email_id = "yogeswaran374@gmail.com"
mobile_number = "+880 01235987684"
Telephone_number = "+12835628365"
password = ")(*yogesYOG237f("

print(validate_email_address(email_id))
print(validate_mobile_number_of_bangladesh(mobile_number))
print(validate_telephone_number_of_USA(Telephone_number))
print(validate_password(password))
