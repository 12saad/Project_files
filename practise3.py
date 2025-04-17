hrs=input("Enter Hours:")
rate=input("Enter Rate:")
try:
    hrs=float(hrs)
    rate=float(rate)
except:
    print("Error, please enter numeric input")

if hrs>40:
    print(rate*40+(hrs-40)*1.5*rate)
else:
    print(hrs*rate)