from GraphInterface import GraphInterface


class Point:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z


class Node:
    tag = 0.0

    def __init__(self, key: int, p: Point):
        self.key = key
        self.p = p


class Edge:
    def __init__(self, src: int, dest: int, weight: float):
        self.weight = weight
        self.src = src
        self.dest = dest


class DiGraph(GraphInterface):
    countMC = 0
    countE = 0
    countV = 0
    nodeMap: dict
    edgeMap: dict
    edgeMapRev: dict

    def __init__(self):
        pass

    def v_size(self) -> int:
        return DiGraph.countV

    def e_size(self) -> int:
        return DiGraph.countE

    def get_mc(self) -> int:
        return DiGraph.countMC

    def get_all_v(self) -> dict:
        return self.nodeMap

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.edgeMapRev[id1]

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.edgeMap[id1]

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 != id2 and id1 in self.nodeMap and id2 in self.nodeMap and id2 not in self.edgeMap[id1]:
            e = Edge(id1, id2, weight)
            self.edgeMap[id1][id2] = e
            self.edgeMapRev[id2][id1] = e
            self.countMC += 1
            self.countE += 1
            return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        p = Point(pos[0], pos[1], pos[2])
        n = Node(node_id, p)
        if node_id not in self.nodeMap:
            self.countMC += 1
            self.countV += 1
            self.nodeMap[node_id] = n
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
        if node_id1 in self.edgeMap and node_id2 in self.edgeMapRev:
            del self.edgeMap[node_id1][node_id2]
            del self.edgeMapRev[node_id2][node_id1]
            self.countMC += 1
            self.countE -= 1
            return True
        return False
