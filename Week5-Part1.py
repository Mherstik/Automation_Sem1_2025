
####
####
print("######\n" *3)
print("CASE STATEMENT")
print("######\n" *3)

lang = input("What's the programming language you want to learn? ")

match lang:
    case "JavaScript":
        print("You can become a web developer.")

    case "Python":
        print("You can become a Data Scientist")

    case "PHP":
        print("You can become a backend developer")

    case "Solidity":
        print("You can become a Blockchain developer")

    case "Java":
        print("You can become a mobile app developer")
    
    case _:
        print("The language doesn't matter, what matters is solving problems.")
        
print("######\n" *3)
print("IF ELIF ELSE statement")
print("######\n" *3)
lang = input("What's the programming language you want to learn? ")

if lang == "JavaScript":
        print("You can become a web developer.")

elif lang ==  "Python":
        print("You can become a Data Scientist")

elif lang ==  "PHP":
        print("You can become a backend developer")

elif lang ==  "Solidity":
        print("You can become a Blockchain developer")

elif lang ==  "Java":
        print("You can become a mobile app developer")
        
else:
        print("The language doesn't matter, what matters is solving problems.")



print("######\n" *3)
print("LOOPS")
print("######\n" *3)
servers = ["a","b","c","a"]

for each in servers:
    print(f"Server {each}")

i = 0
while i < 10:
    i += 1
    print(i)
    