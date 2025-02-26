###
# Get 3 numbers between 1 and 100
# Find the largest
###

# Get a number
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
#     
print(userInput)