x=input("enter number= ")
try:
    x=int(x)
except:
    print("Please enter number")

if x>0:
    print("great job you entered a positive number =",x)