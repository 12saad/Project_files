rate=input("enter your rate=")
hrs=input("enter your hours=")
rate=float(rate)
hrs=int(hrs)
try:
    def calculate(rate,hrs):
        if hrs>40:
            pay=rate*40+(hrs-40)*1.5*rate
            print("pay is",pay)
        else:
            pay=rate*hrs
            print("pay is",pay)
    calculate(rate,hrs)
except:
    print("error in calculation")
    