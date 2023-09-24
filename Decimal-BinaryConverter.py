# So converting from binary to decimal seems quite easy
# 1. first we get the user's binary number and using index[] we can find out if it says 0 or 1 and depending on the if we add that or not
# Converting from decimal to binary might be a bit more difficult
def TurnToInteger(Binary):
    output = 0
    Binary = list(Binary)
    if Binary[0] == "0":
        output += 0 # don't add anything
    else:
        output += 128

    if Binary[1] == "0":
        output += 0 # don't add anything
    else:
        output += 64
        
    if Binary[2] == "0":
        output += 0 # don't add anything
    else:
        output += 32

    if Binary[3] == "0":
        output += 0 # don't add anything
    else:
        output += 16

    if Binary[4] == "0":
        output += 0 # don't add anything
    else:
        output += 8
    
    if Binary[5] == "0":
        output += 0 # don't add anything
    else:
        output += 4
    
    if Binary[6] == "0":
        output += 0 # don't add anything
    else:
        output += 2
    
    if Binary[7] == "0":
        output += 0 # don't add anything
    else:
        output += 1

    print("Your Number Is : " + str(output))

def TurnToBinary(Number):
    binary = ""
    Number = int(Number) # user's number
    placeValue = 1 # this is where we start

    while (placeValue * 2) <= Number:
        placeValue *= 2

    remainder = Number

    while placeValue >= 1: # either 0 or 1
        quotient = int(remainder / placeValue)
        binary += str(quotient)
        remainder = remainder % placeValue
        placeValue = placeValue / 2

    print("Your Binary Is : " + str(binary))
    
# Now that we have our two functions we need to get the user's input for what they would like to convert
a = """
    Hello There! What would you like to do:
    - Convert Binary to Decimal (Please Type "A" )
    - Convert Decimal to Binary (please Type "B  )
"""
userOption = input(a + " :").upper()

if userOption == "A":
    userBinary = input("Please Enter your Binary Number: ")
    for digit in userBinary:
        if digit != "0" and digit != "1":
            # Give the user another chance to reenter the binary
            userBinary = input("Enter just zeros and ones: ")
            break
        else:
            # If the for loop ends naturally, it must be valid so break
            # out of the while loop
            break   
    TurnToInteger(userBinary)
elif userOption == "B":
    userDecimal = int(input("Please Enter your Decimal Number: "))
    TurnToBinary(userDecimal)
else:
    print("Please Type One of the options above (A or B)")
