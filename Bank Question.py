import re
n=int(input())
for i in range(n):
    a=input()
    if bool(re.match(r"^[456][0-9]{15}",a)):
        print("Valid")
    elif bool(re.match(r"^[456][0-9]{3}\-[0-9]{4}\-[0-9]{4}\-[0-9]{4}",a)):
        print("Valid")
    else:
        print("Invalid")
