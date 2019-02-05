a=int(input())
b=int(input())
for num in range(a,b+1):
	order=len(str(num))
	temp=num
	sum=0
	while (temp>0):
		x=temp%10
		sum=sum+x**order
		temp//=10
	if(num==sum):
		print(num)
