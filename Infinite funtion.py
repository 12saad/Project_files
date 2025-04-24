large=0
small=None
while True:
    number=input("enter number=")
    if number=="done":
        break
    try:
        number=float(number)
    except:
        print("enter a valid number")
        continue
    if large<number:
        large=number
    if small is None or small>number:
        small=number
print("smallest number =",small,"largest number",large)
        