import csv

with open('names.csv', 'a', newline='') as csvfile:
    headerList = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=headerList)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'last_name': 'Spam', 'first_name': 'Lovely'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
