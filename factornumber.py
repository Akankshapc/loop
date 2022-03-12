#factornmbr

n=int(input("enter num"))
print("factors are:")
i=1
while i<=n:
	if n%i==0:
		print(i)
	i=i+1
