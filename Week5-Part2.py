###
# Get 3 numbers between 1 and 100
# Find the largest
###

# Get a number
def getNumber():
    userInput = ''

    while userInput.isdigit() == False:
        userInput = input ("Give me a number between 1 & 100: ")
    #     if int(userInput) > 100 or int(userInput) < 1:
    #         print("Please make it an integer between 1 and 100!")
        try:
            userInput = int(userInput)
            if userInput > 100 or userInput < 1:
                print("Between 1 and 100!")
                userInput = ''
                # continue
            else:
                break
        except ValueError:
            print("Please make it an integer between 1 and 100!")
        except:
            Print("Something went wrong")
         
    print(userInput)
    return userInput

# We could get the number by calling the
# function 3 times.
# a = getNumber()
# b = getNumber()
# c = getNumber()

# That's boring...
# Let's use a list!!

userList = []
while len(userList) < 3:
    print(f"User list is length: {len(userList)}")
    userInput = getNumber()
    userList.append(userInput)
    print(userList)

for mumsChickenDInner in userList:
    print(mumsChickenDInner)







