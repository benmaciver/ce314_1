import re
#ex1
pattern = r'(?:\d+(?:,|\.)?\d+(?:bn|m)?(?:\seuros|\seuro|p))|(?:(?:£|\$)\d+(?:,|\.)?\d+(?:bn|m)?)'

a = open("bbctxt.txt","r")
bbcText = a.read()



matches = re.findall(pattern, bbcText)
print(matches)


#ex2
pattern = r'(?:(?:(?:(?:(?:\+1)|2|3)-))?(?:\(\d{3}\))?(?:\s|\-))?(?:\d(?:\.|-|\s)?)+'

c = open("phone_numbers.txt","r")
phonebook = c.read()

matches = re.findall(pattern, phonebook)
for match in matches:
    print(match)

    #matches every phone number correctly except 2nd and 3rd
