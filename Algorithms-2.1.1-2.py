jfile = open('jobs.txt','r')
njobs = int(jfile.readline())
jobs = []
for jno in range(0,njobs):
    jobs.append(list(map(int,(jfile.readline().split()))))
jobs.sort(key = lambda arr : (arr[1]-arr[0],-arr[0]))
lnt = 0; objf1 = 0
for jno in range(0,njobs):
    lnt = lnt + jobs[jno][1]
    objf1 = objf1+ jobs[jno][0] * lnt
jobs.sort(key = lambda arr : arr[1]/arr[0])
lnt = 0; objf2 = 0
for jno in range(0,njobs):
    lnt = lnt + jobs[jno][1]
    objf2 = objf2 + jobs[jno][0] * lnt