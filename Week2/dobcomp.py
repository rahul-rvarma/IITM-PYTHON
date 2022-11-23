d1 = input()
d2 = input()
n1=input().lower()
n2=input().lower()
if d1[6:] < d2[6:]:
  print(n1)
  print(d1)
elif d1[6:]> d2[6:]:
  print(n2)
  print(d2)
elif d1[6:]==d2[6:]:
  if d1[3:4] < d2[3:4]:
    print(n1)
    print(d1)
  elif d1[3:4] > d2[3:4]:
    print(n2)
    print(d2) 
  elif d1[3:4] == d2[3:4]:
    if d1[0:1] < d2[0:1]:
      print(n1)
      print(d1)
    elif d1[0:1] > d2[0:1]:
      print(n2)
      print(d2)
    elif d1[0:1] == d2[0:1]:
      if n1 < n2:
        print(n2)
        print(d2)
      else:
        print(n1)
        print(d1)