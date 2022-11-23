a=input().lower()
b="abcdefghijklmnopqrstuvwxyz"
t=" "
for c in a:
  if c in b:
    t=t+c
print(t)
    