# -*- coding: utf-8 -*-

from calc import Calculator
data=input("Type you calculation f.e.'6+5'\n")
#print(data)
char=["+","-","/","*"]
newdata=[]
cond=True

while cond:
    for ch in char:
        #print(ch)
        newdata=data.split(ch)
        #print(len(newdata))
        if len(newdata)==2:
            cond=False
            break
#print(newdata)
for d in newdata:
    try:
        newdata[0]=float(newdata[0])
        newdata[1]=float(newdata[1])
    except ValueError:
        print('errror!')
        break
    else:
        c=Calculator(newdata[0],newdata[1])
        actionlst=[c.Add(),c.Sub(),c.Mul(),c.Div()]
        cond=True
        while cond:
for i, character in enumerate(char):
    print("----")
    if ch == character:
        print(actionlst[i])
        break
        
