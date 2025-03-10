#create empty dict
gro = {}
#loop frv
while True:
    try:
#get user input
        item = input().upper()
#check if item is already in da dict
        if item in gro:
            gro[item]+= 1
        else:
            gro[item] = 1
#if it is, add 1 in the count
# otherwise, add the item for the first time
    except EOFError:
        for key in sorted(gro.keys()):
            print(gro[key], key)
        break
# print all the items in alphabetical order
#  stop da loop

