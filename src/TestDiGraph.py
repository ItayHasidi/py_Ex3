import unittest
from DiGraph import DiGraph


class MyTestCase(unittest.TestCase):

    def test_v_size(self):
        g: DiGraph = DiGraph()
        for i in range(20):
            g.add_node(i)
        for i in range(20):
            for j in range(4):
                if i != j:
                    g.add_edge(i, j, i + j)
        self.assertEqual(20, g.v_size())

    def test_e_size(self):
        g: DiGraph = DiGraph()
        for i in range(20):
            g.add_node(i)
        for i in range(20):
            for j in range(4):
                if i != j:
                    g.add_edge(i, j, i + j)
        self.assertEqual(76, g.e_size())

    def test_get_mc(self):
        g: DiGraph = DiGraph()
        for i in range(20):
            g.add_node(i)
        for i in range(20):
            for j in range(4):
                if i != j:
                    g.add_edge(i, j, i + j)
        self.assertEqual(96, g.get_mc())

    def test_all_in_edges_of_node(self):
        g: DiGraph = DiGraph()
        for i in range(20):
            g.add_node(i)
        for i in range(20):
            for j in range(4):
                if i != j:
                    g.add_edge(i, j, i + j)
        self.assertEqual(19, len(g.all_in_edges_of_node(0)))

    def test_all_out_edges_of_node(self):
        g: DiGraph = DiGraph()
        for i in range(20):
            g.add_node(i)
        for i in range(20):
            for j in range(4):
                if i != j:
                    g.add_edge(i, j, i + j)
        self.assertEqual(3, len(g.all_out_edges_of_node(0)))

    def test_add_node(self):
        g: DiGraph = DiGraph()
        for i in range(20):
            g.add_node(i)
        for i in range(20):
            for j in range(4):
                if i != j:
                    g.add_edge(i, j, i + j)
        g.add_node(100)
        g.add_node(100)
        self.assertEqual(21, g.v_size())
        g.remove_node(100)
        g.remove_node(100)
        self.assertEqual(20, g.v_size())

    def test_add_edge(self):
        g: DiGraph = DiGraph()
        for i in range(20):
            g.add_node(i)
        for i in range(20):
            for j in range(4):
                if i != j:
                    g.add_edge(i, j, i + j)
        g.add_node(100)
        g.add_node(101)
        g.add_edge(100, 101, 201)
        g.add_edge(100, 101, 201)
        self.assertEqual(77, g.e_size())
        g.remove_node(100)
        g.remove_node(101)
        self.assertEqual(76, g.e_size())

    def test_remove_node(self):
        g: DiGraph = DiGraph()
        for i in range(20):
            g.add_node(i)
        for i in range(20):
            for j in range(4):
                if i != j:
                    g.add_edge(i, j, i + j)
        g.add_node(100)
        self.assertEqual(21, g.v_size())
        g.remove_node(100)
        self.assertEqual(20, g.v_size())

    def test_remove_edge(self):
        g1: DiGraph = DiGraph()
        for i in range(20):
            g1.add_node(i)
        for i in range(20):
            for j in range(4):
                if i != j:
                    g1.add_edge(i, j, i + j)
        g1.add_node(100)
        g1.add_node(101)
        g1.add_edge(100, 101, 201)
        self.assertEqual(77, g1.e_size())
        # g.remove_node(100)
        g1.remove_node(101)
        self.assertEqual(76, g1.e_size())


if __name__ == '__main__':
    unittest.main()
