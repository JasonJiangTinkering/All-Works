
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 09:23:55 2019

@author: jrj2143
"""
x = []
import math
locations = {}

locationsfile = open("ttrvertices.txt")
locitem = locationsfile.readlines()
for y in locitem:
    x = y.split(',', 1)
    locations[x[0]] = x[1].strip(',').strip()
x.clear()
#print(locations)
    
#locations{} has all locations and cords

edges = {}
hold2name = ''
holdcords = ''
holdsplitcords = []
holdx1 = 0
holdy1 = 0
holdx2 = 0
holdy2 = 0
holdname1 = ''
holdname2 = ''
holddis = 0
edgesfile = open("ttredges.txt")
edgeitem = edgesfile.readlines()

print()
for y in edgeitem:

    hold2name = y.split(",")
    holdname1 = hold2name[0]
    holdcords = locations[holdname1]
    holdsplitcords = holdcords.split(",")
    holdx1 = int(holdsplitcords[0])
    holdy1 = int(holdsplitcords[1])
    holdname2 = hold2name[1].strip()
    holdcords = locations[holdname2]
    holdsplitcords = holdcords.split(",")
    holdx2 = int(holdsplitcords[0])
    holdy2 = int(holdsplitcords[1])
    holddis = math.sqrt(math.pow(holdx1 - holdx2, 2) + math.pow(holdy1 - holdy2, 2)) 
    hold2name = holdname1 +' '+  holdname2
    edges[hold2name] = holddis
    
#print(edges)

#uncomment when done
#start = input('what is the starting location')
#goal = input('what is the starting location')

#comment when done
starta = 'Vancouver'
goal  = 'LittleRock'




#alorithom to find paths to goal


#locations that need to be branched on
placesfound = [starta]
distances = [0]


z = []
e = 0
holdu = ' '
previous = ['end']

w = ''
pathe = []

def findpath(location):

#    print(location)
    if previous[placesfound.index(location)] == starta:
        pathe.append(starta)
#        print("kfs;",pathe)
                
    else:
        pathe.append(location)
        lk = placesfound.index(location)
        findpath(previous[lk])
#totaldis reps the longest distance to a place in places found
def isgoal(start, totaldis = 0, points = 36, path= []):
    if points != len(placesfound):
        
        for y in placesfound:
#            print(1)
            for l in edges:
#                print(1)
                z = l.split()
                for item in z:
#                    print('item:', item)
                    if z.index(item) == 0:
                        e = 1
                    else:
                        e = 0
                    
                    if item == y and z[e] not in placesfound:
                            
                        placesfound.append(z[e])
                        distances.append(totaldis + int(edges[l]))
                        previous.append(item)
#                        print(z[e])
                                 
                    elif z[e] in placesfound:
                        totaldis += int(edges[l])
                        indexs = placesfound.index(z[e])
                        if totaldis < distances[indexs]:
                            z.pop(z.index(item))
                            distances[indexs] = totaldis
                            previous[indexs] = item
        

        
                
    findpath(goal)
    print(pathe[::-1])
    return(str(distances[placesfound.index(goal)]), pathe)
                

    
            
        
#calling fun
print(isgoal(starta, 0))
#
#

##
##        #found starting value
##        if start in y:
##            foundplaces.append(x)
##            for q in foundplaces:
##                o = y.split()
##                if float(edges[y]) < shortest:
##                    shortest = edges[q]
##                    holdu = q         
##            if shortest
##
##
##
##                if o[1] == goal:
##                    potential[y] = edges[y]
##                    #potential has all the locations with goal in it
##                    print(potential)
##                    
##                elif o[1] != goal:
##           clear list o
##                    isgoal(o[1], goal)
##
##    print(foundplaces)    
##isgoal(start, goal)      
##edges has all edges and their length