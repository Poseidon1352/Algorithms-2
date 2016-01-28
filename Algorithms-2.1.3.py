jfile = open('edges.txt','r')
[nV,nE] = list(map(int,(jfile.readline().split())))
edgs = []
for edno in range(0,nE):
    edgs.append(list(map(int,(jfile.readline().split()))))
X = [0]*(nV+1); X[1] = 1
T = 0
for i in range(1,nV):
    minLen = float('inf')
    for j in range(0,nE):
        if X[edgs[j][0]] ^ X[edgs[j][1]] == 1 and edgs[j][2] < minLen:
            minLen = edgs[j][2]
            if X[edgs[j][0]] == 0:
                newV = edgs[j][0]
            else:
                newV = edgs[j][1]
    X[newV] = 1
    T = T + minLen
print(T)