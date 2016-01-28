class DSI(object):
	def __init__(self, vno):
		self.vno = vno
		self.head = self
		self.next = self
		self.prev = self
		self.csiz = 1

def Find(a):
	return a.head

def Union(a,b,nC):
	if Find(a) == Find(b):
		return nC
	else:
		if a.head.csiz >= b.head.csiz:
			bigCI = a
			smlCI = b
		else:
			smlCI = a
			bigCI = b
		smlCItail = smlCI.head.prev
		bigCI.head.prev.next = smlCI.head
		smlCI.head.prev = bigCI.head.prev
		smlCItail.next = bigCI.head
		bigCI.head.prev = smlCItail
		bigCI.head.csiz = bigCI.head.csiz + smlCI.head.csiz
		cur = smlCI.head
		while cur.head != bigCI.head:
			cur.head = bigCI.head
			cur = cur.next
		return nC - 1

#Problem 1
# jfile = open('clustering1.txt','r')
# nV = int(jfile.readline())
# nC = nV ; k = 4 ; Vs = [] ; Es = []
# for i in range(0,nV+1):
# 	Vs.append(DSI(i))
# for line in jfile:
#     Es.append(list(map(int,(line.split()))))

# Es.sort(key = lambda arr : arr[2])
# while nC != k:
# 	E = Es.pop(0)
# 	nC = Union(Vs[E[0]],Vs[E[1]],nC)
# while Find(Vs[E[0]]) == Find(Vs[E[1]]):
# 	E = Es.pop(0)
# print(E)

# Problem 2
kfile = open('clustering_big.txt','r')
[nV,nB] = list(map(int,(kfile.readline().split())))
Vs = {} ; hdm = []
for i in range(0,nV):
	pnt = int(kfile.readline().replace(" ",""),2)
	Vs[pnt] = DSI(pnt)
nC = len(Vs)
for i in range(0,nB):
	for j in range(0,i+1):
		hdm.append(1<<i|1<<j)

for vx,obj in Vs.items():
	for msk in hdm:
		pnt = vx^msk
		if pnt in Vs:
			nC = Union(Vs[pnt],obj,nC)
print(nC)