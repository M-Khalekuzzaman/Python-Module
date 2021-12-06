# match() & search() using

import re
pattern = r"colour"
text1 = "Red is a colour,I love red colour,therefor i also love green colour"

'''
if re.match(pattern,text) :
    print("Match")

else:
    print("Not Match")
'''

'''
if re.search(pattern,text) :
    print("String is Match")

else:
    print("String is not match")
'''

'''
match = re.search(pattern,text)
if match :
    print(match.start())
    print(match.end())
    print(match.span())

'''
text2 = re.sub(pattern, "color", text1, count= 2 )
print(text1)
print(text2)