n=int(input())
prime= True
for i in range(2,n):
  if n%i==0:
    prime=False
if prime:
  print( "PRIME")
else:
    print(" not prime")