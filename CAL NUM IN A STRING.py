def demso(S, n):
    count = 0
    len_n = len(str(n))
    i = 0
    while i < len(S):
        if S[i:i+len_n] == str(n):
            count += 1
            i += len_n
        else:
            i += 1
    return count


        # Đếm số lần xuất hiện của N trong S
for _ in range(int(input())):
    s = input().strip()
    n = int(input())
    print(demso(s,n))