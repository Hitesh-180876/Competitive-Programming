# CP Lab 16 
# Hitesh Kumar Sharma
# 180876

class Pair:
	def __init__(self, first, second):
		self.first = first
		self.second = second
infi = 1000000000;

class Node:
	def __init__(self, vertexNumber):	
		self.vertexNumber = vertexNumber
		self.children = []
    
	def Add_child(self, vNumber, length):
		p = Pair(vNumber, length);
		self.children.append(p);
	

def dijkstraDist(g, s, path):
	dist = [infi for i in range(len(g))]
	visited = [False for i in range(len(g))]
	
	for i in range(len(g)):	
		path[i] = -1
	dist[s] = 0;
	path[s] = -1;
	current = s;

	sett = set()	
	while (True):
		
		# Mark current as visited
		visited[current] = True;
		for i in range(len(g[current].children)):
			v = g[current].children[i].first;		
			if (visited[v]):
				continue;

			# Inserting into the
			# visited vertex
			sett.add(v);
			alt = dist[current] + g[current].children[i].second
			if (alt < dist[v]):	
				dist[v] = alt;
				path[v] = current;	
		if current in sett:		
			sett.remove(current);	
		if (len(sett) == 0):
			break;

		# The new current
		minDist = infi;
		index = 0;

		# Loop to update the distance
		# of the vertices of the graph
		for a in sett:	
			if (dist[a] < minDist):		
				minDist = dist[a];
				index = a;		
		current = index;
	return dist;

def printPath(path, i, s):
	if (i != s):
		if (path[i] == -1):	
			print("Path not found!!");
			return;	
		printPath(path, path[i], s);
		print(path[i] + " ");
    
if __name__=='__main__':
	
	v = []
	n = 4
	s = 0;
	for i in range(n):
		a = Node(i);
		v.append(a);

	v[0].Add_child(1, 1);
	v[0].Add_child(2, 4);
	v[1].Add_child(2, 2);
	v[1].Add_child(3, 6);
	v[2].Add_child(3, 3);
	path = [0 for i in range(len(v))];
	dist = dijkstraDist(v, s, path);

	for i in range(len(dist)):
		if (dist[i] == infi):
		
			print("{0} and {1} are not " +
							"connected".format(i, s));
			continue;	
		print("Distance of {}th vertex from source vertex {} is: {}".format(
						i, s, dist[i]));
	
