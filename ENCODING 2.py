p='ABDEFGHIJKLMNOPQRSTUVWXYZ_.'
def fk(i):
    return p.index(i)

while True:
    s = input()
    if s[0] == "0" :
        break
    k,s = s.split()
    new_vt =[p[(fk(i) + int(k)) % 28] for i in s]
    print(''.join(reversed(new_vt)))
