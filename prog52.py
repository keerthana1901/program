no=input()
if no==no[::-1]:
    print("yes")
else:
    value1=no.strip("0")
    
    if value1==value1[::-1]:
        print("yes")
    else:
        value1=no.lstrip("0")
        
        if value1==value1[::-1]:
            print("yes")
        else:
            print("no")
