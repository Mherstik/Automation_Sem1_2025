### do a divide by something

a = 12


### do tests for errors
def getNum():
    # while True:
        b = input("Gimme a number: ")
        try:
            b = int(b)
            print(a / b)
            # break
        except ValueError:
            print("You gave an incorrect value.\nTry again")
            getNum()
        except ZeroDivisionError:
            print("You gave me zero.\nTry again")
            getNum()
##
getNum()
print("It finished")
##

## Print error
# x = 5
# y = 0
# z = x/y
# print("Division", c)

## Assertion

password = "SuperSecret"
password1 = "SuperSecret1"
password2 = "SuperSecret22"

if password == "SuperSecret":
    print("Password incorrect")

# Uncomment these to see the error printed or not.
# The second part is printed when the assert statement fails.
# assert password == 'SuperSecret', 'password should be different0'
# assert password1 == 'SuperSecret1', 'password should be different1'
# assert password2 == 'SuperSecret2', 'password should be different2'

## Logging warning

import logging
x = 7
y = 0
logging.warning("This is an error")
