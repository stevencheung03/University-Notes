G = {"A": ["B"],"B": ["A", "C"], "C": ["B"]} # the graph
n = "A" # the start node
visited = [] # the set of visited nodes
todo = [n] # the list o nodes we need to visit


while len(todo) != 0:
	m = todo[0]
	todo = todo[1:]
	print(m)
	visited.append(m)
	for x in G[m]:
		if x not in visited:
			if x not in todo:
				todo.append(x)