# import numpy as np
x= float(input("Enter the value of X: "))
w= float(input("Enter the value of weight W: "))
b= float(input("Enter the value of bias b: "))
net= int(w*x+b)
if (net<0):
    out= 0
elif((net>=0)&(net<=1)):
    out=net
else:
    out=1
    print("net=", net)
    print("output=", out)