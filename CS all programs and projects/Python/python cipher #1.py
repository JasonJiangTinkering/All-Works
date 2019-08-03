#this code is from stuy ccc's problem set, which I have been working on to learn python in prep for SHAPE
#Jason Jiang 7/11/19 python project #3
#the goal: take 2 inputs, a string and a int to make a caesar cipher, moving each char (int) amount of times
email = input ("What is the email you want ciphered")
move = input ("How many digits do you want the digits to move")
x = []
print(email)
for z in email:
    if z == " ":
        x.append(z)
        continue
    else:
        y = int(ord(str(z)))
        print(y)
        y += int(move)
        y = chr(y)
        x.append(y)
        print(x)

    
final = " "
for p in x:
    final += p

print(final)


#what i have learned
#u cannot copy paste code from google docs as "" and tabs must be manually inputed
#unlike java to instigate a var u dont need to cast it + ; and {} are not needed
#ord = str -> ASCII
#chr = ASCII ->
#u can use a for loop to iterate through a string where the index var are char within the string
