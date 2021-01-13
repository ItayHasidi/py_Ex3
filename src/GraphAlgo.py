from typing import List

from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
from abc import ABC
import json
import matplotlib.pyplot as plt

import random as ran
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
                # print(len(i))
                if len(i) == 1:
                    x: dict = i
                    # print(x.get('id'))
                    t: int = x.get('id')
                    # print(type(t))
                    self.graph.add_node(t)
                else:
                    # print(i['pos'])
                    p = str.split(i['pos'], ',')
                    t: int = i['id']
                    self.graph.add_node(t, p)

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

            temp2 = self.graph.nodeMap.get(i)
            if temp2 is None:
                t2: dict = {'id': i}
            else:
                str = temp2[0]+','+temp2[1]+','+temp2[2]
                t2: dict = {'pos': str, 'id': i}
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

    def dfs(self, key: int):
        stackIN = [key]
        stackOUT = [key]
        resIN = [key]
        resOUT = [key]
        res = []

        visitedIN = {key: True}
        visitedOUT = {key: True}
        while len(stackOUT) != 0:
            temp = stackOUT.pop()
            for i in self.graph.all_out_edges_of_node(temp):
                # print(type(i))
                # print(i)
                # print(visitedOUT.get(i))
                if visitedOUT.get(i) is not True:
                    stackOUT.append(i)
                    visitedOUT[i] = True
                    resOUT.append(i)

        while len(stackIN) != 0:
            temp = stackIN.pop()
            for i in self.graph.all_in_edges_of_node(temp):
                if visitedIN.get(i) is not True:
                    stackIN.append(i)
                    visitedIN[i] = True
                    resIN.append(i)

        for i in resIN:
            for j in resOUT:
                if i == j:
                    res.append(i)
        self.compList.append(res)
        return res

    def connected_component(self, id1: int) -> list:
        for i in self.compList:
            for j in i:
                if id1 == j:
                    # print(i)
                    return i
        return self.dfs(id1)

    def connected_components(self) -> List[list]:
        for i in self.graph.get_all_v():
            self.connected_component(i)
        return self.compList

    def plot_graph(self) -> None:
        z = self.graph.v_size() * self.graph.v_size()
        # plt.axis([0,1000000,0,10000000])
        for i in self.graph.get_all_v():
            if self.graph.nodeMap.get(i) is None:
                x = (i * (i - 1)) / 2
                y = i
                plt.plot([x], [y], 'o')
                plt.annotate(str(i), xy=(float(x), float(y)))
                self.plot_Edge(i, 1)

            else:
                p = self.graph.nodeMap.get(i)
                x = p[0]
                y = p[1]
                # print(x,y)
                plt.plot([float(x)], [float(y)], 'o')
                plt.rcParams.update({'font.size': 18})
                plt.annotate(str(i), xy=(float(x), float(y)))
                self.plot_Edge(i, 0)
        # if self.graph.nodeMap.get(i) is None:
        #     for i in self.graph.get_all_v():

        plt.show()

    def plot_Edge(self, id1: int, flag: int):
        p_s = dict()
        x_s = float()
        y_s = float()
        p_d = dict()
        x_d = float()
        y_d = float()
        for i in self.graph.all_out_edges_of_node(id1):
            if flag == 0:
                p_s = self.graph.nodeMap.get(id1)
                x_s: float = p_s[0]
                y_s: float = p_s[1]
                p_d = self.graph.nodeMap.get(i)
                x_d = p_d[0]
                y_d = p_d[1]

            elif flag == 1:
                x_s = (id1 * (id1 - 1)) / 2
                y_s = id1
                x_d = (i * (i - 1)) / 2
                y_d = i

            x_d: float = float(x_d) - float(x_s)
            y_d: float = float(y_d) - float(y_s)
            plt.arrow(float(x_s), float(y_s), float(x_d), float(y_d),
                      width=0.000005, head_width=0.0002, length_includes_head=True)
