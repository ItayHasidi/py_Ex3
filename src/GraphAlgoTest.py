import unittest

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):

    def test_get_graph(self):
        g: DiGraph = DiGraph()
        for i in range(20):
            g.add_node(i)
        for i in range(20):
            for j in range(4):
                if i != j:
                    g.add_edge(i, j, i + j)
        mc1 = g.countMC
        e1 = g.countE
        v1 = g.countV
        ga = GraphAlgo(g)
        mc2 = ga.get_graph().countMC
        e2 = ga.get_graph().countE
        v2 = ga.get_graph().countV
        self.assertEqual(mc1, mc2)
        self.assertEqual(e1, e2)
        self.assertEqual(v1, v2)


    def test_save_load_from_json(self):
        g = GraphAlgo()
        self.assertTrue(g.load_from_json("../data/A0"))
        mc1 = g.get_graph().countMC
        e1 = g.get_graph().countE
        v1 = g.get_graph().countV
        self.assertTrue(g.save_to_json("../data/save_load_test.json"))
        mc2 = g.get_graph().countMC
        e2 = g.get_graph().countE
        v2 = g.get_graph().countV
        self.assertEqual(mc1, mc2)
        self.assertEqual(e1, e2)
        self.assertEqual(v1, v2)

    def test_shortest_path(self):
        g = GraphAlgo()
        g.load_from_json("../data/A0")
        self.assertEqual(2.5507493954969362, g.shortest_path(0, 9)[0])

    def test_connected_component(self):
        g = GraphAlgo()
        g.load_from_json("../data/A0")
        self.assertEqual(11, len(g.connected_component(0)))

    def test_connected_components(self):
        g = GraphAlgo()
        g.load_from_json("../data/A0")
        self.assertEqual(11, len(g.connected_components()[0]))


if __name__ == '__main__':
    unittest.main()
