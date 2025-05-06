// Aim: 1.1.1. Area of Circle - Algorithm and Flowchart


r = float(input('Enter the radius : '))
PI = 3.14
if(r < 0):
	print('Enter a positive value upto 100')
else:
	a = PI * r * r
	print('Area of circle = %.6f'%(a))
