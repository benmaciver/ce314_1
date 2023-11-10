import re
pattern = r'(?:\d+(?:,|\.)?\d+(?:bn|m)?(?:\seuros|\seuro|p))|(?:(?:£|\$)\d+(?:,|\.)?\d+(?:bn|m)?)'

a = open("bbctxt.txt","r")
bbcText = a.read()
b = open("test.txt","r")
testText = b.read()


matches1 = re.findall(pattern, bbcText)
print(matches1)
matches2 = re.findall(pattern, testText)
print(matches2)

