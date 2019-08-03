x = int(input("Input number to convert"))

y = []
while x > 0:
    if x%2 == 1:
        y.insert(0,"1")
        x//=2
        print(x)
    
    elif x%2 == 0:
        y.insert(0,"0")
        x//=2
        print(x)

    
    



print(''.join(y))
