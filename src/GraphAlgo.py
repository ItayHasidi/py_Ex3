from typing import List

from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
from abc import ABC
import json
import matplotlib.pyplot as plt

from src import GraphInterface


class GraphAlgo(GraphAlgoInterface, ABC):
    # graph: GraphInterface
    # graph: DiGraph()
    # tags: dict

    def __init__(self, g: DiGraph = None):
        self.graph = DiGraph()
        if g is not None:
            self.graph = g
        self.tags = dict()
        self.countVisit = 0
        self.stack = []
        self.chkMC = 0
        self.compList = []

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        with open(file_name) as jFile:
            data = json.load(jFile)
            # print(data['Nodes'])
            for i in data['Nodes']:
                x: dict = i
                # print(x.get('id'))
                t: int = x.get('id')
                # print(type(t))
                self.graph.add_node(t)

            for i in data['Edges']:
                src = i['src']
                dest = i['dest']
                w = i['w']
                self.graph.add_edge(src, dest, w)
            return True
        return False

    def save_to_json(self, file_name: str) -> bool:
        data = dict()
        data['Edges'] = []
        data['Nodes'] = []
        for i in self.graph.get_all_v():
            for j in self.graph.all_out_edges_of_node(i):
                temp = self.graph.all_out_edges_of_node(i).get(j)
                # print(temp)
                t = dict()
                t['src'] = i
                t['dest'] = j
                # print("check" + temp[1])
                t['w'] = temp

                data['Edges'].append(t)
            temp2 = self.graph.get_all_v()
            t2: dict = {'pos': temp2, 'id': i}
            data['Nodes'].append(t2)
        with open(file_name, 'w') as out:
            json.dump(data, out)
            return True
        return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if id1 != id2:
            if self.graph.get_all_v().__contains__(id1) and self.graph.get_all_v().__contains__(
                    id2):  # check if this happens
                q = []
                self.setTag(-1)
                for i in self.graph.all_out_edges_of_node(
                        id1):  # sets all neighbors of id1 in a queue and gives them a weight
                    q.append(i)
                    self.tags[i] = self.graph.all_out_edges_of_node(id1).get(i)
                while len(q) != 0:
                    node = q.pop(0)
                    tempTag = self.tags.get(node)
                    for i in self.graph.all_out_edges_of_node(node):
                        dis = self.graph.all_out_edges_of_node(node).get(i)
                        if self.tags.get(i) < 0 or self.tags.get(i) > (tempTag + dis):
                            self.tags[i] = (tempTag + dis)
                            q.append(i)
                l = []
                l.append(id2)
                last = id2
                # print(self.tags.get(id2))
                if self.tags.get(id2) != -1:
                    for j in self.graph.get_all_v():
                        for i in self.graph.all_in_edges_of_node(last):
                            # print("i: " + str(i) + ", tag of i: " + str(self.tags.get(i)) + ", last: " + str(last) + ", distance to last: " + str(
                            #     self.graph.all_in_edges_of_node(last).get(i)))
                            dis = self.tags.get(i) + self.graph.all_in_edges_of_node(last).get(i)
                            if dis == self.tags.get(last):
                                l.append(i)
                                last = i
                                break
                        l.append(id1)
                        l.reverse()
                        return self.tags.get(id2), l
                else:
                    return float('inf'), []
        return 0, []

    def setTag(self, val: int):
        for i in self.graph.get_all_v():  # resets all the tags to 0
            self.tags[i] = val

    def connected_component(self, id1: int) -> list:
        if id1 in self.graph.get_all_v():
            mc = self.graph.get_mc()
            if self.chkMC == 0 or self.chkMC != mc:
                self.connected_components()
            for i in self.compList:
                # print("type of i is: " + str(type(i)))
                for j in i:
                    if id1 == j:
                        return i
        return []


    def connected_rek_out(self, id1 : int ) :
        self.countVisit += 1
        for i in self.graph.all_out_edges_of_node(id1):
            if self.tags.get(i) == -1:
                self.tags[i] = 0
                self.connected_rek_out(i)
        self.stack.append(id1)
        self.tags[id1] = self.countVisit
        self.countVisit += 1

    def connected_rek_in(self, id1: int, l: list()):
        l.append(id1)
        self.tags[id1] = 0
        for i in self.graph.all_in_edges_of_node(id1):
            if self.tags.get(i) == -1:
                self.connected_rek_in(i, l)
        return l

    def connected_components(self) -> List[list]:
        endList = []
        self.chkMC = self.graph.get_mc()
        self.setTag(-1)
        for i in self.graph.get_all_v():
            if self.tags.get(i) == -1:
                self.connected_rek_out(i)

        self.countVisit = 0
        self.setTag(-1)
        # print(self.stack)
        while len(self.stack) != 0:
            temp = self.stack.pop(len(self.stack)-1)
            if self.tags.get(temp) == -1:
                l = []
                self.connected_rek_in(temp, l)
                endList.append(l)
        self.compList = endList
        return endList



    def plot_graph(self) -> None:
        pass
