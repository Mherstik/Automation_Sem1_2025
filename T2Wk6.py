import csv

# import time
# print("Going to sleep")
# time.sleep(3)
name = input("What's your name: ")
age = input("What's your age: ")
postcode = input("What's your postcode: ")


filename = 'Testing.csv'

def addRow():
    newPerson = [name, age, postcode]
    with open(filename, mode = 'a') as csvfile:
        csvWriter = csv.writer(csvfile)
        csvWriter.writerow(newPerson)
        csvfile.close()

### Read the table and compare all lines
def compareCSV():                                   
    with open(filename, mode = 'r') as csvfile:
        csvReader = csv.DictReader(csvfile)
        for row in csvReader:
            print(row)
            if name == row['Name'] and age == row['Age']:
                print(f"{name} and {age} matches data in row!")
                
            else:
                print("Moving on")

compareCSV()

#    addRow()

# a = ['Cavoodle','Chihuahua','Labrador']
# 
# b = input("Give me a dog type: ")
# c = input("Another: ")
# 
# if b and c in a:
#     print(f"The dog {b} and {c} is already in the list")
# else:
#     print(f"The dog {b} is not in the list")
#     
# print("Done IF, now doing for")
#     
# for each in a:
#     if each.lower() == b.lower():
#         print(f"The dog {b} is already in the list as {each}")
#     else:
#         print(f"{b} is not {each}")
