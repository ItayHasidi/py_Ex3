from DiGraph import DiGraph
# from GraphAlgo import GraphAlgo
import json
import time
import networkX

from src.GraphAlgo import GraphAlgo


def tester(s: str, g: GraphAlgo):
    print(s)
    ms1 = time.time()
    g.shortest_path(0,9)
    ms2 = time.time()
    print(ms2-ms1)


if __name__ == '__main__':
    g_algo = GraphAlgo()
    # file = '../data/Graphs_on_circle/G_10_80_1.json'
    # g_algo.load_from_json(file)
    # tester("node = 10", g_algo)
    # file = '../data/Graphs_on_circle/G_100_800_1.json'
    # g_algo.load_from_json(file)
    # tester("node = 100", g_algo)
    # file = '../data/Graphs_on_circle/G_1000_8000_1.json'
    # g_algo.load_from_json(file)
    # tester("node = 1000", g_algo)
    # file = '../data/Graphs_on_circle/G_10000_80000_1.json'
    # g_algo.load_from_json(file)
    # tester("node = 10000", g_algo)
    # file = '../data/Graphs_on_circle/G_20000_160000_1.json'
    # g_algo.load_from_json(file)
    # tester("node = 20000", g_algo)
    file = '../data/Graphs_on_circle/G_30000_240000_1.json'
    g_algo.load_from_json(file)
    tester("node = 30000", g_algo)
