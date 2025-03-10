def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # two letters
    if s[0].isalpha() == False and s[1].isalpha() == False:
        return False
    # contain 6 characters, minimum 2 characters
    if len(s) < 2 or len(s) > 6:
        return False
    # number can't be in the middle, must come at the end
    #the first num can't be 0
    i = 0
    while i < len(s):
        if s[i] == '0':
            return False
        else:
            break
    i += 1
   # no periods, spaces, marks
    for c in s:
        if c in ['.', ' ', '!', '?']:
            return False
    return True

main()
