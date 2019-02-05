n=int(input())
temp=n
sum=0
while (temp>0):
	a=temp%10
	sum = sum+a**3
	temp//=10
if(n==sum):
	print("yes")
else:
	print("no")
