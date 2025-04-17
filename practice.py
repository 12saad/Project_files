hrs=input("Enter Hours: ")
rate=input("Enter Rate: ")
try:
    hrs=int(hrs)
    rate=float(rate)
    total=hrs*rate
    print("Pay:",total)
except ValueError:
    print("Error, please enter numeric input")