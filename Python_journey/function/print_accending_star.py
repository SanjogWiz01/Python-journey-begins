'''a=int(input("how many star you want"))
for i in range(1,a+1):
    print("*"*i)'''
def acstar(n,x):
    if n > x:
        return
    else:
        print('*'*n)
        return acstar(n+1, x)

x = int(input("enter the no of star you want: "))
acstar(1, x)        