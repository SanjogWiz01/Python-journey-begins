# def star(int x):
# for(i=1;i<x;i++):
# print("* \t",end"")
# return star(x-1)



# a=int(input("enter the no of decreasing star you want"))
# result=star(a)
# print("take this :",result)
def star(x):
    if x <= 0:
        return
    for i in range(1, x + 1):
        print("*\t", end="")
    print()  # move to next line after printing stars
    return star(x - 1)


a = int(input("Enter the no of decreasing stars you want: "))
star(a)
# Example usage: