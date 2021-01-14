# Ex3

We are building a directed weighted graph implementation with a number of features and classes.
 
We have 2 classes:
- DiGraph
- GraphAlgo

###  DiGraph:

+	add_node - add a new node if he doesn't exist.
+	add_edge - connects between id1 to id2 with the edge but just to one way!
+	get_all_v - give all the nodes in the graph.
+	all_in_edges_of_node - gives all the outgoing edges of a node.
+ all_out_edges_of_node - gives all the incoming edges of a node.
+	remove_node - delete the node.
+	remove_edge - delete all the edges between this node and the others nodes.
+	v_size - the number of nodes.
+	e_size - the number of edges.
+	get_mc - counts all add/delete actions made on nodes and edges.


### GraphAlgo:

+	get_graph - return graph.
+	setTag - sets the tag of all nodes to a given value.
+	shortest_path - give a list of the way from id1 to id2 and the distance between them.
+	reverse graph - make all the edge turning over.
+	save_to_json - saves the whole graph on a file, including all nodes and all edges with their weight.
+ load_from_json - creates a new graph according to a save file.
+ dfs - a DFS function that finds all the nodes that are attached to key, it does it once for all incoming nodes, and once for outgoing nodes. and eventually takes all   the nodes that are in both groups and returns them as a list.
+ connected_component - calls to dfs() to calculate the SCC that the node id belongs to. if the a list that contains the node id exists, the function will return that   list without calling to dfs().
+ connected_components - sends all the nodes of the graph to connected_component(), so to find all the SCCs that exist.
+ plot_graph - using matplotlib, this function creates a visual demonstration of the graph. if the nodes do not have a (x,y) value, the function will print them in an   elegant manner.
+ plot_Edge - this function helps plot_Graph() to print the graph. it prints all the edges of the graph.

	
