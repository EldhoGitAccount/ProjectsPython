def div40by(dividedBy) :
    try :
        return 40/dividedBy;
    except ZeroDivisionError :
        print('Error: you tried to divide by zero')

print(div40by(2))
print(div40by(0))      
