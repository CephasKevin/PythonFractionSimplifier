print("Python started")

simplificationMade = "true"
simplifiedNumer = 0
simplifiedDenom = 0


def isItAnInteger(x):#Checks if the entered variable is a whole number
    if x == int(x):
        return "Y"
    elif x != int(x):
        return "N"


def simplifyFraction(numer, denom):
    
    i = 2
    #Go through the four fundamental numbers 2,3,5,7
    while i < 8:

        numerDivided = numer / i
        denomDivided = denom / i

        if isItAnInteger(numerDivided) == "Y" and isItAnInteger(denomDivided) == "Y":
            print(str(numer) + " divided by " + str(i) + " is " + str(numerDivided))
            print(str(denom) + " divided by " + str(i) + " is " + str(denomDivided))

            numer = numerDivided
            global simplifiedNumer
            simplifiedNumer = numerDivided
            

            denom = denomDivided
            global simplifiedDenom
            simplifiedDenom = denomDivided
            

        else:
            print("bad division...")    

        if i != 2:
            i = i + 2
        elif i == 2:
            i = i + 1    

while simplificationMade == "true":
    
    global simplifiedNumer
    global simplifiedDenom

    preSimplifiedNumer = simplifiedNumer
    preSimplifiedDenom = simplifiedDenom

    if simplifiedNumer != 0 or simplifiedDenom != 0:
        simplifyFraction(simplifiedNumer, simplifiedDenom)
      
    else:
        
        simplifyFraction(-1080, 240)#ENTER NUMERATOR AND DENOMATOR HERE RESPECTIVELY

    if preSimplifiedNumer == simplifiedNumer or simplifiedNumer == 2 or preSimplifiedDenom == simplifiedDenom or simplifiedDenom == 2:
        simplificationMade = "false"         


if simplifiedNumer == 0 or simplifiedDenom == 0:
    print("Fraction already in simplest form!")
else:
    print("simplified Numerator = " + str(simplifiedNumer))
    print("simplified Denomenator = " + str(simplifiedDenom))    


    
   


print("")
print("Python Ended")