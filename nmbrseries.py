#series Q-20
num=int(input("enter num"))
f=1
s=1
i=1
while i<=num:
	f=f*i
	s=s+1/f
	i=i+1
print("sum of sequence =",s)
