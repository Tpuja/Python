string = input ("Enter the String")
count = 0
count2 = 0
for i in string:
    if (i.islower()):
        count = count +1
    elif(i.isupper()):
        count2 = count2 +1
print ("The number of lower case character is:")
print (count)
print ("The number of uppercase character is:")
print (count2)