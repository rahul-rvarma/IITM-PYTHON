s = input()
word=" "
n = len(s)
if n%2 == 0:
  if s[-1]==".":
    word= s[:-1]
  print(word)
  elif s[-1] != ".":
    word = s.append(".")
  print(word)              
else:
  print(s)