#1038 - Snack
x,y=map(int,input().split())
if x==1:
    a=4.00*y
    print("Total: R$ %.2f"%a)
elif x==2:
    a=4.50*y
    print("Total: R$ %.2f"%a)
elif x==3:
    a=5.00*y
    print("Total: R$ %.2f"%a)
elif x==4:
    a=2.00*y
    print("Total: R$ %.2f"%a)
elif x==5:
    a=1.50*y
    print("Total: R$ %.2f"%a)
