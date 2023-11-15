import re
#ex1
pattern = r'(?:\d+(?:,|\.)?\d+(?:bn|m)?(?:\seuros|\seuro|p))|(?:(?:£|\$)\d+(?:,|\.)?\d+(?:bn|m)?)'#re pattern for currency

a = open("bbctxt.txt","r")
bbcText = a.read()#reads the bbc article
b = open("test.txt","r")
testText = b.read()#some test data from the assignment brief to test for more ways to type currency



matches = re.findall(pattern, bbcText)
print(matches)
matches = re.findall(pattern, testText)
print(matches)
#prints every time this re is matched in both texts


#ex2
#re for phone numbers
pattern = r'(?:(?:(?:(?:(?:\+1)|2|3)-))?(?:\(\d{3}\))?(?:\s|\-))?(?:\d(?:\.|-|\s)?)+'

c = open("phone_numbers.txt","r")#phone numbers from assignment brief
phonebook = c.read()

matches = re.findall(pattern, phonebook)
for match in matches:
    print(match)
    #prints each match in a list

    #matches every phone number correctly except 2nd and 3rd
