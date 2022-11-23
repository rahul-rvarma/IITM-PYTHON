s = str(input())
a =s.lower()
vow=""
if "a" in a:
  vow=vow+"a"
if "e" in a:
  vow=vow+"e"
if "i" in a:
  vow=vow+"i"
if "o" in a:
  vow=vow+"o"
if "u" in a:
  vow=vow+"u"
if vow !=" ":
  print(vow)
else:
  print("none")