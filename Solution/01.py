l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print("The number divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included) which is Seperated by comma: "+' , '.join(l))