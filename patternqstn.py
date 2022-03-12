a=int(input('enter num'))
i=1
while i <= a :
	c=1
	while c <= a - i:
		print(' ',end=' ')
		c+=1
	j=i
	while j>=1:
		print(j,end=' ')
		j-=1
	print( )
	i+=1
