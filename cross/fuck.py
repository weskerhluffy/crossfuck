'''
Created on 18/07/2018

@author: ernesto
'''

# XXX: https://app.codesignal.com/arcade/code-arcade/labyrinth-of-nested-loops/W5Sq7taLSzNHh8GiF/description

from collections import defaultdict
from itertools import permutations
from functools import partial
from email.policy import default


class palabra():

    def __init__(self, word):
        self.word = word
        self.posiciones = defaultdict(list)
        self.distancias = defaultdict(partial(defaultdict, partial(defaultdict,lambda: 0)))
        self.__initiliaze__()

    def __initiliaze__(self):
        for i, c in enumerate(self.word):
            self.posiciones[c].append(i)
            
        for c1 in self.posiciones:
            for d1 in self.posiciones[c1]:
                for c2 in self.posiciones:
                    for d2 in self.posiciones[c2]:
                        d = d2 - d1
                        if d > 1:
                            self.distancias[c1][c2][d]+=1
        cadr = []
        for c1 in self.distancias:
            cads = []
            for c2 in self.distancias[c1]:
                cads.append("{}:{}".format(c2, self.distancias[c1][c2]))
            cadr.append("{}->{}".format(c1, " ".join(cads)))

#        print("{} dist\n{}".format(self.word,"\n".join(cadr)))
    def __repr__(self):
#        return "{}:{}".format(self.word,self.distancias)
        return "{}".format(self.word)


def contar_formaciones(pa, pb, pc, pd):
    r = 0
    for ai in range(len(pa.word)):
#        print("ai {}".format(ai))
        cai = pa.word[ai]
#        print("posiciones de cai {} en {} {}".format(cai,pb.word,pb.posiciones[cai]))
        for bi in pb.posiciones[cai]:
#            print("bi {}".format(bi))
            assert cai == pb.word[bi]
            if bi < len(pb.word) - 2:
                for aj in range(ai + 2, len(pa.word)):
#                    print("aj {}".format(aj))
                    dh = aj - ai
                    caj = pa.word[aj]
#                    print("posiciones de caj {} en {} {}".format(caj,pc.word,pc.posiciones[caj]))
                    for ci in pc.posiciones[caj]:
#                        print("ci {}".format(ci))
                        assert caj == pc.word[ci]
                        if ci < len(pc.word) - 2:
                            for bj in range(bi + 2, len(pb.word)):
                                cbj = pb.word[bj]
                                dv = bj - bi
                                cj = ci + dv
                                if cj < len(pc.word):
                                    ccj = pc.word[cj]
#                                    print("cbj {}:{} ccj {}:{}".format(cbj,bj,ccj,cj))
#                                    print("ai {} cai {} aj {} caj {} bi {} ci {} bj {} cbj {} cj {} cbj {}".format(ai,cai,aj,caj,bi,ci,bj,cbj,cj,ccj))
#                                    print("dh {} dists {}".format(dh,pd.distancias[cbj][ccj]))
                                    if dh in pd.distancias[cbj][ccj]:
#                                        print("valida: {} {} {}".format((ai, aj), (bi, bj), (ci, cj) ))
                                        r += pd.distancias[cbj][ccj][dh]
    return r

            
def crosscaca(ps):
    p1 = ps[0]
    p2 = ps[1]
    p3 = ps[2]
    p4 = ps[3]
    r = 0
    for p1i in range(len(p1)):
        for p2i in range(len(p2)):
            for p1j in range(len(p1)):
                dh = p1j - p1i
                for p3i in range(len(p3)):
                    for p2j in range(len(p2)):
                        dv = p2j - p2i
                        p3j = p3i + dv
                        for p4i in range(len(p4)):
                            p4j = p4i + dh
                            if p1j > p1i + 1 and p2j > p2i + 1 and p3j + p3i + 1 and p4j > p4i + 1 and p3j < len(p3) and p4j < len(p4) and p1[p1i] == p2[p2i] and p1[p1j] == p3[p3i] and p2[p2j] == p4[p4i] and p3[p3j] == p4[p4j]:
                                r += 1
#                                print("valida c: {} {} {} {}".format((p1i, p1j), (p2i, p2j), (p3i, p3j), (p4i, p4j)))
    return r


def crosswordFormation(words):
    pals = list(map(palabra, words))
    perputas = permutations(pals)
    r = 0
    for pe in perputas:
#        print("perp {}".format(pe))
        rt = contar_formaciones(pe[0], pe[1], pe[2], pe[3])
#        rt1 = crosscaca(list(map(lambda p:p.word, pe)))
#        print("rt {}".format(rt))
#        print("rt1 {}".format(rt1))
#        assert rt == rt1
        r += rt
    return r


if __name__ == '__main__':
    words = ["africa", "america", "australia", "antarctica"]
    crosswordFormation(words)
