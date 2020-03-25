lmb = ['$']
final = [False] * 1010

def lmbNFA(cuvant, i, stare):
    global ok
    if ok:
        return

    if i == len(cuvant):
        if final[stare]:
            ok = 1
        return

    if trans[stare]['$'] != [-1]:
        for st in trans[stare]['$']:
            lmbNFA(cuvant, i, st)

    if trans[stare][cuvant[i]] == [-1]:
        return
    for st in trans[stare][cuvant[i]]:
        lmbNFA(cuvant, i + 1, st)

with open("lmbNFA.in") as f:
    n = int(f.readline())
    m = int(f.readline())
    lmb.extend(f.readline().split())
    q0 = int(f.readline())
    k = int(f.readline())
    stari_finale = [int(x) for x in f.readline().split()]
    for stare in stari_finale:
        final[stare] = True
    stari_finale.clear()

    trans = [{x: [-1] for x in lmb} for i in range(0, n)]
    l = int(f.readline())
    for i in range(l):
        x, a, y = f.readline().split()
        if trans[int(x)][a] == [-1]:
            trans[int(x)][a] = [int(y)]
        else:
            trans[int(x)][a].append(int(y))

    for test in range(7):
        cuvant = f.readline().rstrip()
        ok = 0
        lmbNFA(cuvant, 0, q0)
        if ok:
            print(f"Cuvantul {cuvant} este acceptat!")
        else:
            print(f"Cuvantul {cuvant} nu este acceptat!")