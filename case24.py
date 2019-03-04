num=int(input())
sum=0
number1=num
while(number1>0):
	a=number1%10
	sum=sum*10+a
	number1=number1/10
print(sum)
