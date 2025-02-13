#     Input: numbers a, b, c
#     Output: largest number
#     Read a, b, c
#

def checkInput():
    userInput = ''
    while userInput.isdecimal() == False:
        userInput = input("Give me a number: ")
    userInput = int(userInput) 
    return userInput

# while True:
#     a = input("Give me the first number: ")
#     try:
#         a = int(a)
#         break
#     except:
#         print("That's not a number!")
# print(type(a), a)

print("Give me three numbers")
print("First number")
a = checkInput()
print("Second number")
b = checkInput()
print("Third number")
c = checkInput()
print(a,b,c)

if a <= 0:
    print(f"{a} is too small")
elif a > 100:
    print(f"{a} is too big")
else:
    print("Something")

#print(f" First number is {a}\n",
#      f"Second number is {b}\n",
#      f"Third number is {c}")
#     largest = a
#     if b > a
#     	largest = b
#     if c > b
#     	largest = c
#     Output largest