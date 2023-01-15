char= input("Enter the character")
if char.lower() in ('a', 'e','i', 'o', 'u'):
    print(char, "is vowel")
elif char.upper() in ('A', 'E', 'I', 'O', 'u'):
    print(char, "is a Vowel")
else:
    print (char, "is Consonant")
