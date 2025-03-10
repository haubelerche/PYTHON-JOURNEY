a = input("What is Answer to the Great Question of Life, the Universe, and Everything?")
if a.strip() == "42":
    print("Yes")
elif a.lower().strip() == "forty-two":
    print("Yes")
elif a.lower().strip() == "forty two":
    print("Yes")
else:
    print("No")
