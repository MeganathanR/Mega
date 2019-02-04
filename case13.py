num=int(input())
prime=1
i=2
while i<num:
	if(num%i==0):
		prime=0
	i=i+1	
if(prime==1):
	print("yes")
else:
	print("no")
