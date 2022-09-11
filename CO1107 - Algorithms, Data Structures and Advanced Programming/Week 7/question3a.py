adj_list = {}
mylist = []
def add_node(node):
	if node not in mylist:
		mylist.append(node)
	else:
		print("Node ",node," already exists!")

def add_edge(node1, node2, weight):
	temp = []
	if node1 in mylist and node2 in mylist:
		if node1 not in adj_list:
			temp.append(node2)
			adj_list[node1] = temp, weight
		elif node1 in adj_list:
			temp.extend(adj_list[node1])
			temp.append(node2)
			adj_list[node1] = temp, weight
		else:
			print("Nodes don't exist!")

def graph():
	for node in adj_list:
		print(node, [i for i in adj_list[node]])


#Adding nodes
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_node("F")
add_node("G")

#Adding edges
add_edge("A","B", 20)
add_edge("B","C", 7)
add_edge("B","G", 2)
add_edge("C", "B", 7)
add_edge("C","E", 1)
add_edge("C","D", 1)
add_edge("G", "B", 2)
add_edge("G","F", 15)
add_edge("E", "C", 1)
add_edge("E","D", 9)
add_edge("E","F", 3)
add_edge("D", "C", 1)
add_edge("D","E", 9)
add_edge("D","F", 2)

#Printing the graph
graph()

#Printing the adjacency list
print(adj_list)