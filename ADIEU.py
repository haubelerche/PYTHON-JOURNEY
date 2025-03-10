import inflect
p = inflect.engine()

namelist = []
while True:
    try:
        name = input("Name: ").title().strip()
        namelist.append(name)
    except EOFError:
        break
mylist = p.join(namelist)
print("Adieu, adieu, to " + mylist)
