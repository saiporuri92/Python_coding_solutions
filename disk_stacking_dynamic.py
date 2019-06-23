def diskStacking(disks):
    # Write your code here.
	disks.sort(key = lambda disk : disk[2])
	mapp = {}
    maxheight = 0
	maxindex = None
	for i,v in enumerate(disks):
		mapp[i] = [v[2],[i]]
	for i,v in enumerate(disks):
		for disk in range(i):
			if disks[disk][0] < v[0] and disks[disk][1] < v[1]:
				if mapp[disk][0] + v[2] > mapp[i][0]:
					mapp[i] = [mapp[disk][0] + v[2],mapp[disk][1] + [i]]
        if mapp[i][0] > maxheight:
            maxheight = mapp[i][0]
            maxindex = i
	result = [disks[i] for i in mapp[maxindex][1]]
	return result
print(diskStacking([[2,1,2],[3,2,3],[2,2,8]]))