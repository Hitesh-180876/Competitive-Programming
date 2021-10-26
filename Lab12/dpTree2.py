""" Python code to find the maximum path length
 considering any node as root
 
 """

# Lab 12
# Competitive Programming
# Hitesh Kumar Sharma
# 180876


inn = [0] * 100
out = [0] * 100

# function to pre-calculate the array inn[]
# which stores the maximum height when travelled
# via branches

def dfs1(v, u, parent):
	global inn, out
	
	# initially every node has 0 height
	inn[u] = 0

	# traverse in the subtree of u
	for child in v[u]:

		# if child is same as parent
		if (child == parent):
			continue

		# dfs called
		dfs1(v, child, u)

		# recursively calculate the max height
		inn[u] = max(inn[u], 1 + inn[child])

# function to pre-calculate the array ouut[]
# which stores the maximum height when traveled
# via parent

def dfs2(v, u, parent):
	global inn, out
	
	# stores the longest and second
	# longest branches
	mx1, mx2 = -1, -1

	# traverse in the subtress of u
	for child in v[u]:
		if (child == parent):
			continue

		# compare and store the longest
		# and second longest
		if (inn[child] >= mx1):
			mx2 = mx1
			mx1 = inn[child]

		elif (inn[child] > mx2):
			mx2 = inn[child]

	# traverse in the subtree of u
	for child in v[u]:
		if (child == parent):
			continue

		longest = mx1

		# if longest branch has the node, then
		# consider the second longest branch
		if (mx1 == inn[child]):
			longest = mx2

		# recursively calculate out[i]
		out[child] = 1 + max(out[u], 1 + longest)

		# dfs function call
		dfs2(v, child, u)

# function to prall the maximum heights
# from every node
def printHeights(v, n):
	global inn, out
	
	# traversal to calculate inn[] array
	dfs1(v, 1, 0)

	# traversal to calculate out[] array
	dfs2(v, 1, 0)

	# prall maximum heights
	for i in range(1, n + 1):
		print("The maximum height when node", i, "is considered as root is", max(inn[i], out[i]))

# Driver Code
if __name__ == '__main__':
	n = 11
	v = [[] for i in range(n + 1)]

	# initialize the tree given in the diagram
	v[1].append(2)
	v[2].append(1)
	v[1].append(3)
	v[3].append(1)
	v[1].append(4)
	v[4].append(1)
	v[2].append(5)
	v[5].append(2)
	v[2].append(6)
	v[6].append(2)
	v[3].append(7)
	v[7].append(3)
	v[7].append(10)
	v[10].append(7)
	v[7].append(11)
	v[11].append(7)
	v[4].append(8)
	v[8].append(4)
	v[4].append(9)
	v[9].append(4)

	# function to print the maximum height from every node
	printHeights(v, n)
