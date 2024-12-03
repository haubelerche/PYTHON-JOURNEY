for _ in range(int(input())):
    def char(n):
        for i in n:
            if i not in ['0','1','2']:
                return "NO"
        return "YES"
    print(char(input()))

