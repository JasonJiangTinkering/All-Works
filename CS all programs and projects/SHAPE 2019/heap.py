# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 09:41:45 2019

@author: jrj2143
"""

class Heap():
    
    def __init__(self):
        self.test = []


    def add(self, item):
        self.test.append(item)
        if len(self.test) != 1:
#            print(1,self.test.index(item)//2)
#            print(3,self.test[self.test.index(item)//2][0])
#            print(4,item[0])
#            print('test:',self.test)
#            print(len(self.test))
#            print(self.test[(len(self.test)-1)//2][0])
#            print(self.test[len(self.test)-1][0])
            status = False
            while status == False:
#                print(3,self.test[self.test.index(item)//2][0])
#                print(4,item[0])
#                print(self.test[self.test.index(item)//2][0]> item[0])
#                self.test[self.test.index(item)//2], self.test[self.test.index(item)] = self.test[self.test.index(item)], self.test[self.test.index(item)//2]
#                print(self.test[self.test.index(item)])
#                print(self.test)
#                print('hi')
#                swap child and parent items untill it satifies the heap
                
                if self.test[self.test.index(item)//2][0] <= item[0]:
                    status = True
                    
                    print('test:',self.test)              
                    continue
                y = self.test.index(item)
                x = self.test.index(item)//2 

                self.test[y], self.test[x] = self.test[x], self.test[y]
                
#                print(self.test)
            
                print(3,self.test[self.test.index(item)//2][0])
                print(4,item[0])
                
            else: return()
        
    def pop(self):
        x = 0
        y = self.test.pop(0)
        self.test.insert(0, (999, 1234))
        while x != (len(self.test) - 1) or x != len(self.test) - 2:
            if len(self.test) >= (x + 1)*2:
                print(x)
                print((x+ 1)*2)
                sw = int((x + 0.5)*2) - 1
                swa = int((x + 1)*2) - 1
                if self.test[int((x +.5) *2)-1][0] >= self.test[((x+1) *2)-1][0]:
                    self.test[swa], self.test[x] = self.test[x], self.test[swa]
                    x = (x + 1) *2
                else:
                    self.test[sw], self.test[x] = self.test[x],self.test[sw]
                    x = int((x + 0.5)*2)
            else: break
        print(self.test)
        return(y)
        
        
        
        
print('start')
x = Heap()
x.add((3, 'test'))
x.add((2, 'test2'))
x.add((1, 'test3'))
x.add((5, 'test5'))
print(x.pop())