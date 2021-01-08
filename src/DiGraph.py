from GraphInterface import GraphInterface
from abc import ABC


class DiGraph(GraphInterface):

    def __init__(self):
        self.countMC = 0
        self.countE = 0
        self.countV = 0
        self.nodeMap = dict()
        self.edgeMap = dict()
        self.edgeMapRev = dict()

    def v_size(self) -> int:
        return self.countV

    def e_size(self) -> int:
        return self.countE

    def get_mc(self) -> int:
        return self.countMC

    def get_all_v(self) -> dict:
        return self.nodeMap

    def all_in_edges_of_node(self, id1: int) -> dict:
        if id1 in self.edgeMapRev:
            return self.edgeMapRev[id1]

    def all_out_edges_of_node(self, id1: int) -> dict:
        if id1 in self.edgeMap:
            return self.edgeMap[id1]

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 is not id2:
            if id1 in self.nodeMap:
                if id2 in self.nodeMap:
                    if id2 not in self.edgeMap(id1):#.__contains__(id2):
                        self.edgeMap[id1][id2] = weight
                        self.edgeMapRev[id2][id1] = weight
                        # self.edgeMap[id1] = {id2: weight}
                        # self.edgeMapRev[id2] = {id1: weight}
                        # self.edgeMap[id1], [id2] = e
                        # self.edgeMapRev[id2], [id1] = e
                        self.countMC += 1
                        self.countE += 1
                        return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        # if pos is not None:
        #     p = Point(pos[0], pos[1], pos[2])
        # else:
        #     p = Point(0, 0, 0)
        # n = Node(node_id, p)
        if node_id not in self.nodeMap:
            self.countMC += 1
            self.countV += 1
            # self.nodeMap.__setitem__(node_id, pos)
            self.nodeMap[node_id] = pos
            self.edgeMap[node_id] = {}
            self.edgeMapRev[node_id] = {}
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.nodeMap:
            # this removes node_id from its neighbors
            for i in self.edgeMap[node_id]:
                del self.edgeMapRev[i][node_id]
            # this removes node_id's neighbors from it
            for i in self.edgeMapRev[node_id]:
                del self.edgeMap[i][node_id]
            del self.edgeMap[node_id]
            del self.edgeMapRev[node_id]
            del self.nodeMap[node_id]
            self.countMC += 1
            self.countV -= 1
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 in self.edgeMap and node_id2 in self.edgeMap[node_id1] \
                and node_id2 in self.edgeMapRev and node_id1 in self.edgeMapRev[node_id2]:
            del self.edgeMap[node_id1][node_id2]
            del self.edgeMapRev[node_id2][node_id1]
            self.countMC += 1
            self.countE -= 1
            return True
        return False
