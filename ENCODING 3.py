def countchar(s):
    dict = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            dict += str(count) + s[i-1]
            count = 1
    dict += str(count) + s[-1]
    return dict

t = int(input())
for _ in range(t):
    s = input()
    print(countchar(s))

    