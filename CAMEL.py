#prompt camelcase
c = input("camelCase: ")
print("snake_case: ", end="")
for char in c:
    if char.isupper():
        print("_"+char.lower(), end="")
    else:
        print(char, end="")
#print snake

#loop through letters to find the upper letter
print()





