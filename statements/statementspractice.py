#try / except

# Example 1
try:
    text = 'hello'
    text[0] = 'm'
    print(text)
except TypeError as e:
    print(e)
finally:
    print('I happen regardless of any exceptions.')
# Example 2
try:
    print(x)
except NameError as e:
    print(e, ' because x is not initiated')
finally:
    print('I happen regardless of any exceptions.')



#print list
def print_list(list):
    for i in range(len(list)):
        print(list[i])
    pass


lst1 = [1, 2, 5, 1429]
lst2 = ['this', 'list', 'is', 'being', 'printed']
lst3 = ['there', 'are', 2, 'data', 'types', 'being', 'printed']
lst4 = [[1, 2], ['hello', 'from', 'within']]
print_list(lst1)        # 1 2 5 1429
print_list(lst2)        # this list is being printed
print_list(lst3)        # there are 2 data types being printed
print_list(lst4)        # [1, 2] ['hello', 'from', 'within']


#check member
def check_membership(guest_name, guest_list):
    return guest_name in guest_list



guest_list = ["George", "Anthony", "Susan", "Tiffany"]
print(check_membership("Sally", guest_list))        # False
print(check_membership("Anthony", guest_list))



#penny doubling
print("** Doubling Penny **")

# How many times would a penny need to double to generate a million dollars?
count = 0
total = .01

# STEP 2: Write the while loop
while total<=1000000:
    count+=1
    total*=2


    print('Double', count, 'times')

# How much money has been generated at that point?
    print('${:,}'.format(total))



# hex check

def is_valid_hex_code(code):
    if code[0] != "#" or len(code)!=7:
        return False
    for i in [1,2,3,4,5,6]:
        if ord(code[i].upper()) < 48 or ord(code[i].upper()) > 70:
            return False
        elif ord(code[i].upper()) >57 and ord(code[i].upper()) < 65:
            return False
    return True


print(is_valid_hex_code("#CD5C5C")) #> True
print(is_valid_hex_code("#EAECEE")) #> True
print(is_valid_hex_code("#eaecee")) #> True

print(is_valid_hex_code("#CD5C58C"))
# Prints False
# Length exceeds 6

print(is_valid_hex_code("#CD5C5Z"))
# Prints False
# Not all alphabetic characters in A-F

print(is_valid_hex_code("#CD5C&C"))
# Prints false
# Contains unacceptable character

print(is_valid_hex_code("CD5C5C"))
# Prints False
# Missing #


#sequence code

def seq_of_numbers(numstr):
    seq=''
    count=1
    for i in range(len(numstr)):
        if i==len(numstr)-1:
            seq+=(str(count)+numstr[i])
        elif numstr[i]!=numstr[i+1]:
            seq+=(str(count)+numstr[i])
            count=1
        else:
            count+=1
    return seq



print(seq_of_numbers("1211"))
# This is "one 1, one 2, two 1s"
# Prints "111221"

print(seq_of_numbers("111221"))
# This is "three 1s, two 2s, and one 1"
# Prints "312211"

print(seq_of_numbers("31131211131221"))
# This is "one 3, two 1s, one 3, one 1, one 2, three 1s,
#    one 3, one 1, two 2s, and one 1"
# Prints "13211311123113112211"



#turn uppercase chars into a space and a lowercase
def cap_space(phrase):
    result = ''
    for char in phrase:
        if char.isupper():
            result+=(' '+char.lower())
        else:
            result+=char
    return result


print(cap_space("helloWorld"))     #> "hello world"
print(cap_space("iLoveMyTeapot"))  #> "i love my teapot"
print(cap_space("stayIndoors"))    #> "stay indoors"


#regex check zip code format

import re

def valid_zip_code(zip):
    x = re.findall("[0-9]{5}(-[0-9]{4})?$", zip)
    if x != []:
        return zip
    else:
        return "this is not a zip code, buddy"

zip1 = '47243'
zip2 = '23128-'
zip3 = '01237-1238'
zip4 = '91374-31'
zip5 = '1321-9883'
zip6 = '6320'

print(valid_zip_code(zip1))     # '47243'
print(valid_zip_code(zip2))     # "The zip code you entered is invalid"
print(valid_zip_code(zip3))     # '01237-1238'
print(valid_zip_code(zip4))     # "The zip code you entered is invalid"
print(valid_zip_code(zip5))     # "The zip code you entered is invalid"
print(valid_zip_code(zip6))     # "The zip code you entered is invalid"
