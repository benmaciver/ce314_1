import re
pattern = r'(?:£|\$)?\d+(?:,|\.)?\d+(?:bn|m|p)?(?:md\s\beuro\b|\seuros)?'

a = open("bbctxt.txt","r")
bbcText = a.read()
b = open("test.txt","r")
testText = b.read()


matches1 = re.findall(pattern, bbcText)
print(matches1)

