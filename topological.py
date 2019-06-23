def topologicalSort(jobs, deps):
    # Write your code here.
	mapp = {}
	for i in jobs:
		mapp[i] = []
	result = []
	for dep in deps:
		mapp[dep[0]].append(dep[1])
	visited = []
	visiting = set()
	def dfs(node):
		for i in mapp[node]:
			if i not in visited:
				visiting.add(i)
				dfs(i)
				visited.append(i)
	for i in jobs:
		if i not in visited:
			dfs(i)
            visited.append(i)
	return visited[::-1]


print(topologicalSort([1, 2, 3, 4], [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]))