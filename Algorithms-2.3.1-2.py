kfile = open('knapsack1.txt','r')
[W,nI] = list(map(int,(kfile.readline().split())))
itms = [[-1,0]] ; sol = (W+1)*[0]
for i in range(0,nI):
	itms.append(list(map(int,(kfile.readline().split()))))
for i in range(1,nI+1):
	print(i)
	for x in range(W,-1,-1):
		if x >= itms[i][1]:
			sol[x] = max(sol[x],sol[x-itms[i][1]] + itms[i][0])
print(sol[W])
