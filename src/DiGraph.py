from GraphInterface import GraphInterface


class DiGraph(GraphInterface):

    def __init__(self):
        self.countMC = 0
        self.countE = 0
        self.countV = 0
        self.nodeMap = dict()
        self.edgeMap = dict()
        self.edgeMapRev = dict()

    def v_size(self) -> int:
        """
        returns the number of nodes on the graph.
        """
        return self.countV

    def e_size(self) -> int:
        """
        returns the number of edges on the graph.
        """
        return self.countE

    def get_mc(self) -> int:
        """
        returns the number of actions that were made on the graph.
        """
        return self.countMC

    def get_all_v(self) -> dict:
        """
        returns a dictionary containing all the nodes of the graph.
        """
        return self.nodeMap

    def all_in_edges_of_node(self, id1: int) -> dict:
        """
        returns a dictionary containing all the edges that enter the given node id.
        """
        if id1 in self.edgeMapRev:
            return self.edgeMapRev[id1]

    def all_out_edges_of_node(self, id1: int) -> dict:
        """
        returns a dictionary containing all the edges that leave the given node id.
        """
        if id1 in self.edgeMap:
            return self.edgeMap[id1]

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        creates a new edge between id1 and id2 withe the given weight.
        """
        if id1 is not id2:
            if id1 in self.nodeMap and id2 in self.nodeMap:
                if not self.edgeMap.get(id1).__contains__(id2):
                    if weight >= 0:
                        self.edgeMap[id1][id2] = weight
                        self.edgeMapRev[id2][id1] = weight
                        self.countMC += 1
                        self.countE += 1
                        return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        adds a new node to the graph.
        """
        if node_id not in self.nodeMap:
            self.countMC += 1
            self.countV += 1
            self.nodeMap[node_id] = pos
            self.edgeMap[node_id] = {}
            self.edgeMapRev[node_id] = {}
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        """
        removes a node from the graph with the node id.
        removes any attached edges if they exist.
        """
        flag = True
        if node_id in self.nodeMap:
            for i in self.edgeMap[node_id]:
                del self.edgeMapRev[i][node_id]
                self.countE -= 1
                flag = False
            for i in self.edgeMapRev[node_id]:
                del self.edgeMap[i][node_id]
                if flag:
                    self.countE -= 1
            del self.edgeMap[node_id]
            del self.edgeMapRev[node_id]
            del self.nodeMap[node_id]
            self.countMC += 1
            self.countV -= 1
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        removes the edge between id1 and id2.
        """
        if node_id1 in self.edgeMap and node_id2 in self.edgeMap[node_id1] \
                and node_id2 in self.edgeMapRev and node_id1 in self.edgeMapRev[node_id2]:
            del self.edgeMap[node_id1][node_id2]
            del self.edgeMapRev[node_id2][node_id1]
            self.countMC += 1
            self.countE -= 1
            return True
        return False

    def __repr__(self):
        """
        a toString function that returns a string containing all the nodes and edges of the graph.
        """
        res = ""
        for i in self.nodeMap:
            tempNode = self.nodeMap.get(i)
            res += ("Node - id: " + str(i) + ", pos: " + str(tempNode) + "\n")
        for i in self.edgeMap:
            tempEdge: dict = self.edgeMap.get(i)
            for j in tempEdge:
                tempEdge2 = tempEdge.get(j)
                res += ("Edge - src: " + str(i) + ", dest: " + str(j) + ", weight: " + str(tempEdge2) + "\n")
        return res
