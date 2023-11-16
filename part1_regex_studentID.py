import re
#ex1
pattern = r'(?:\d+(?:,|\.)?\d+(?:bn|m)?(?:\seuros|\seuro|p))|(?:(?:£|\$)\d+(?:,|\.)?\d+(?:bn|m)?)'#re pattern for currency

a = open("bbctxt.txt","r")
bbcText = a.read()#reads the bbc article


matches = re.findall(pattern, bbcText)
print(matches)

#prints every time this re is matched


#ex2
#re for phone numbers
pattern = r'(?:(?:(?:(?:(?:\+1)|2|3)-))?(?:\(\d{3}\))?(?:\s|\-))?(?:\d(?:\.|-|\s)?)+'

phone_numbers = ["555.123.4565","+1-(800)-545-2468","2-(800)-545-2468","3-800-545-2468","555-123-3456","555 222 3342","(234) 234 2442","(243)-234-2342","1234567890","123.456.7890","123.4567","123-4567","1234567900","12345678900"]


matches = [re.findall(pattern, number) for number in phone_numbers]
for match in matches:
    print (match)
