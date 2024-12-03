for t in range(int(input())):
    def check(s):
        res=''.join(reversed(s))
        for i in range(1, len(s)):
            if (abs(ord(s[i]) - ord(s[i-1]))) != (abs(ord(res[i]) - ord(res[i-1]))):
                return 'NO'
        return 'YES'
    print(check(input()))