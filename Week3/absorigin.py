x=0
y=0
man=0
c=input()
while c !="STOP":
  if c=="UP":
    y=y+1
  elif c=="DOWN":
    y=y-1
  elif c=="RIGHT":
    x=x+1
  elif c=="LEFT":
    x=x-1
c=input()
man=abs(x)+abs(y)
print(man)
