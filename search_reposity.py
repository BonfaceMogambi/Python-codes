import re

txt = "This is a test. This is only a test."
x = re.findall("man", txt)
if x:
    print("There is a match")  # Output: ['test', 'test']
else:
    print("No match found")

