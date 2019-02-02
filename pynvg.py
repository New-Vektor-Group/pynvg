
class pynvg:

	def __init__(self):
		print("Hello pynvg")

#Returns a list with ORD of symbols
def chrlist(dsa):
    c = 0
    for i in dsa:
        if len(i)!=1:
            break
        else:
            c=1
    if(c==1):
        nlist = []
        for i in dsa:
            nlist.append(ord(i))
        return nlist
    else:
        return "Your list hasn't symbols, but (for example) words"

#Returns a list with ORD of symbols in lists
def chrlists(dsa):
    c = 0
    for i in dsa:
        for j in i:
            if len(j)!=1:
                break
            else:
                c=1
    if(c==1):
        nlist = dsa
        for i in dsa:
            for j in i:
                nlist[dsa.index(i)][i.index(j)] = ord(j)
        return nlist
    else:
        return "Your list hasn't symbols, but (for example) words"

#Returns a list with divided to symbols
def setwlists(ds):
    nds = []
    nids = ""
    for i in ds:
        nids = list(i)
        nds.append(nids)
    return nds

#Returns max count of lists in list
def maxlen(ds):
    for i in range(len(ds)):
        if(i != len(ds)-1):
            if (len(ds[i]) > len(ds[i + 1])):
                c = len(ds[i])
            else:
                c = len(ds[i+1])
    return c

#Returns a list with equal count of elements in lists
def optimise(rds,nn):
    nds = rds
    ika = 0
    for j in rds:
        lj = len(j)
        if nn != lj:
            ika = nn - lj
            for i in range(ika):
                nds[rds.index(j)].append(0)
    return nds