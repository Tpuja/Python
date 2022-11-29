#Puja Thapa
initialdisplay= '''WELCOME TO SUNWAY CHARACTER CHECK SYSTEM MAITIDEVI,KATHMANDU'''
print(initialdisplay)
String = input ("Enter the String: ")
LowerCase = 0
UpperCase = 0
Digit = 0
SpecialLetter = 0 

for ch in String:
    if ch.islower():
        LowerCase = LowerCase + 1
    elif ch.isupper():
        UpperCase = UpperCase + 1
    elif ch.isdigit():
        Digit = Digit +1
    else:
        SpecialLetter = SpecialLetter + 1
print("lower", LowerCase)
print("upper", UpperCase)
print("digit", Digit)
print("special" , SpecialLetter)
print("Thank You For Your Visit")
