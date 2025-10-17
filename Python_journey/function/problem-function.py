def larg(a, s, d):
	if (a > s and a > d):
		print("the greatest number is", a)
	elif (s > a and s > d):
		print("the greatest is :", s)
	else:
		print(d, "is the greatest")

a=int(input("enter the first number"))
s=int(input("enter the second number"))
d=int(input("enter the third number"))
larg(a, s, d)
# def larg(a,s,d):
# if (a>s and a>d):
# print("the greatest number is",a)
# elif(s>a and s>d):
# print("the greatest is :,s)
# print(d,is the greatest)
# larg(1,2,3)