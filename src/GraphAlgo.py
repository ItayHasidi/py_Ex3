from typing import List

from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
from abc import ABC
import json

from src import GraphInterface


class GraphAlgo(GraphAlgoInterface, ABC):
    # graph: GraphInterface
    # graph: DiGraph()

    def __init__(self):
        self.graph = DiGraph(self)

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        with open(file_name) as jFile:
            data = json.load(jFile)
            for i in data['Nodes']:
                pos = i['pos']
                key = i[id]
                self.graph.add_node(key, pos)

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
            for j, value in self.graph.all_out_edges_of_node(i):
                temp = self.graph.all_out_edges_of_node().get(j)
                t: dict = {'src': i, 'w': temp[0], 'dest': temp[1]}
                data['Edges'].append(t)
            temp2 = self.graph.get_all_v()
            t2: dict = {'pos': temp2, 'id': i}
            data['Nodes'].append(t2)
        with open(file_name, 'w') as out:
            json.dump(data, out)
            return True
        return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def connected_component(self, id1: int) -> list:
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:
        pass
