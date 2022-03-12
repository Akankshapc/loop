a=1
while a<=5:
	b=int(input('enter num'))
	if b==5:
		print('wow you guessed correct')
		break
	elif b<5:
		print('number entered by you entered is small ,try one more time')
	else:
		print('number entered by you entered is greater, try one more time')
	a+=1
