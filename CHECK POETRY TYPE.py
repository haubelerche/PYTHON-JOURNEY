dautien, ans, _ = -1, [], input()
try:
    while True:
        l = len(input().split())
        dautien = l
        if l == 6:
            input()
            if l != dautien: ans.append(1)
        else:
            ans.append(2)
            for i in range(3): input()


except: pass
print(len(ans))
for i in ans: print(i)
