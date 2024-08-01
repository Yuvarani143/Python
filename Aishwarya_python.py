size=input("enter the size")
bill=0
if(size=='s' or size== 'S'):
    bill=100
    print("small pizza is 100")
elif(size=='m' or 'M'):
    bill = 200
    print("medium pizza is 200")
else:
    bill = 300
    print("large pizza is 300")
want_pepporini =input("do you want pepporini?")
if(want_pepporini=='y' or want_pepporini=='Y'):
    if(size=='s' or size=='S'):
        bill += 30
    if(size=='m' or size=='M'):
        bill +=50
    else:
        bill += 100
want_cheese=input("do you want extra cheese?")
if(want_cheese=='yes' or want_cheese=='YES'):
    bill += 20
    
print(f"your total bill is {bill}")
