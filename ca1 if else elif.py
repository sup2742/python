a=int (input("enter the number"))
d=int (input("enter the  number"))
b=int (input("enter the  number"))
if(a>b and a>d):
    larger=a
elif(b>a and b>d):
        larger=b
else:
    larger=d
    print("d is greater" ,larger)
