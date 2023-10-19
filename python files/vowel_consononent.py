n = input("Enter number: ")


if not n.isalpha():
    print("Not an alphabet")
elif n.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")