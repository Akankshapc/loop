num=int(input("enter any number"))
b=0
if num==0 or num==1:
	print("not prime")
i=2
while i<num:
	if num%i==0:
		b=b+1
	i=i+1
if b==0:
	print("num is prime")
else:
	print("num is not prime")
