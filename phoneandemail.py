import re

phoneRegex = re.compile(r'''(
  (\d{3}|\(\d{3}\))?              # area code
  (\s|-|\.)?                      # separator
  (\b\d{3}\b)                     # first 3 digits
  (\s|-|\.)                       # separator
  (\d{4})                         # last 4 digits
  (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
  )''', re.VERBOSE)

emailRegex = re.compile(r'''(
  (\w)+
  (@)
  (\w)+
  (\.)
  (\w)+
  )''', re.VERBOSE)

input_file = open("nostarchcomcontactus.txt", "r")
text = input_file.read()
input_file.close()

matches = []
for groups in phoneRegex.findall(text):
  phoneNum = "-".join([groups[1], groups[3], groups[5]])
  if groups[8] != "":
    phoneNum += " x" + groups[8]
  matches.append(phoneNum)
for groups in emailRegex.findall(text):
  matches.append(groups[0])

if len(matches) > 0:
  print("\n".join(matches))
else:
  print("No phone numbers or email addresses found.")

import re

num = re.compile(r"\b\d{3}\b")
text = "4444 is 333 plus 3."
matches = num.findall(text)
print(matches)

