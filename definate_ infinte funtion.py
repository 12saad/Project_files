#smallest=None
#print("smallest number is:", smallest)
#for i in [2,5,9,8]:
    #if smallest is None or i < smallest:
        #smallest=i
        #print("smallest=", smallest)
#print(smallest)

#a=[3,4,5,6,7]
#print(min(a))
total=0
sum=0
while True:
    a=input("enter number=")
    if(a=="done"):
        break
    try:
        a=float(a)
    except:
        print("enter an valid number")
        continue
    total=total+1
    sum=sum+a
print("sum=",a,"average=",a/total)
        