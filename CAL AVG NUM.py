input()
diem = sorted([float(x) for x in input().split()])
s = 0
loc_diem = [x for x in diem if x != diem[0] and x != diem[-1]]
for x in loc_diem:
    s += x
print(f"{s/len(loc_diem):.2f}")