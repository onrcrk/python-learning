company = ["LG", "Arçelik", "Vestel", "Beko", "Siemens"]
for one in company:
    print(one)
print("This one isn't sorted yet. Now, I will sort the list and write them back 2 back.")
company.sort()
for sorted in company:
    print(sorted)
print("Now I want to give numbers to my list. Thats how I enumarate my list.")
print(list(enumerate(company,1)))
print("These ,1 works for giving numbers starting from 1. We can start at the -999")
print(list(enumerate(company,-999)))
print("What we do we want to print our list in one string? That's how it's working")
stringcompany = ", ".join(company)
print(stringcompany)
print("We also can put '-' between the elements.")
stringcompany = "-".join(company)
print(stringcompany)