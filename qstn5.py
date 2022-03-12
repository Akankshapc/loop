i=1
while i<=100:
	if i%3==0:
		print("Nav")
	if i%7==0:
		print("Gurkul")
	if i%3==0 and i%7==0:
		print("NavGurkul")
	else:
		print(i)
	i=i+1
