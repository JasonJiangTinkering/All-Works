#goal: to make a merge sort to sort a unordered list of length (input)

import math
import random

    #building a unordered list to sort

#asking user for length
size = int (input('How long do u want the list to be'))

#adding random ints in the list per size of list
master = []
for y in range(size):
    master.append(random.randint(0, 10))

print(master)

    #building elements for sorting


#building a temp list to hold items before overriding the master
temp = []
#finding how many times we need to itterate to sort the list
times = int(math.log(size, 2)+1)

#finding the size of the group that we are merging at one time
lengths = 1






print((size/lengths)/2)
   #creating sorting algoritom
for x in range(times):
#making pointers for the list
    pointer1 = 0
    pointer2 = lengths
    hold2 = lengths
    
    for y in range(int((size/lengths)/2)):
        hold2 = pointer2
        print(pointer2)
        print(pointer1)
        while pointer1 != pointer2 and pointer2 != (hold2 + lengths):
            if master[pointer1] >= master[pointer2]:
                temp.append(master[pointer2])
                pointer2 += 1
                print(temp)
            if master[pointer2] > master[pointer1]:
                temp.append(master[pointer1])
                pointer1 += 1
                print(temp)
        if pointer1 != pointer2:
            
            while pointer1 != pointer2:
                temp.append(master[pointer1])
                pointer1 += 1
                print(temp)
        if pointer2 != (hold2 + lengths):
            
            while pointer2 != (hold2 + lengths):
                temp.append(master[pointer2])
                pointer2 += 1
                print(temp)
        print(y)
        pointer1 = (2*(y + 1) * lengths)
        pointer2 = (2*(y + 2) * lengths)
    lengths = lengths ** 2
    
    print(temp)
    master.clear()

    for y in temp:
        master.append(y)
    temp.clear()
    print(master)
            
                


