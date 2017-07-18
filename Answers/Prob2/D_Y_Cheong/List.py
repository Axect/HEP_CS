import csv
import operator as op
import math
import matplotlib.pyplot as plt
def In() : 
    reader = csv.reader(open("Phytest.csv"), delimiter = ",")
    my_list = list(reader)
    return my_list

def Remove():
    ilist = In()
    del ilist[0]
    return ilist

def slist():
    dlist = Remove()
    iget0 = op.itemgetter(0)
    
    slist = list(map(iget0, dlist))
    return slist

def flist():
    flist = Remove()
    iget1 = op.itemgetter(1)

    flist = list(map(iget1, flist))
    return flist
    
def convert():
    nlist = flist()
    
    clist = list(map(float, nlist))

    return clist

def mean():
    x = convert()
    mean = sum(x)/(len(x))
    
    return mean

def std():
    clist = convert()
    m = mean()
    ss = sum((x-m)**2 for x in clist)
    std = math.sqrt(ss/len(clist))

    return std

def merge():
    l1 = slist()
    l2 = convert()

    lmerge = list(list(l) for l in zip(l1, l2))
    
    return lmerge

def sort():
    la = merge()

    sorlist = sorted(la, key = op.itemgetter(1), reverse=True)

    return sorlist

def split():
    split = list(map(op.itemgetter(1), sort()))
    return split

def rank(a):
    n = len(a)
    ivec = sorted(range(n),key=a.__getitem__)

    svec= [a[k] for k in ivec]
    sumrank = 0
    dupcount = 0
    newarray = [0]*n
    
    for i in range(n):
        sumrank += i
        dupcount += 1
        if i == n-1 or svec[i] != svec[i+1]:
            for j in range(i-dupcount+1, i+1):
                newarray[ivec[j]] = i+1

            sumrank = 0
            dupcount = 0

    return newarray

print(rank(split()))
def reverse():
    rarray = rank(split())
    n2 = len(rarray)
    

    return [n2-x+1 for x in rarray]


def Finalmerge():
    sflist1 = list(map(op.itemgetter(0),sort()))
    sflist2 = list(map(op.itemgetter(1),sort()))
    rlist = reverse()

    merge = list(list(l) for l in zip(sflist1, sflist2, rlist))


    return merge

def Nowdoit():
    print("Mean is ",mean())
    print("STD is ", std())

    with open('Sorted Phytest.csv', "w", newline="") as f :
        writer = csv.writer(f)
        writer.writerows(Finalmerge())

Nowdoit()

with open('Sorted Phytest.csv','r') as f:
    fopen = list(csv.reader(f))

rank = [i[2] for i in fopen]
score = [i[1] for i in fopen]

plt.title("Score of Exam")
plt.plot(rank, score, label = 'score distribution')
plt.legend(loc='upper left')
plt.xlabel('rank')
plt.ylabel('score')
plt.savefig("Sorted Phytest.png")