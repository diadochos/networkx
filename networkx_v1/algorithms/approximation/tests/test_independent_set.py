from nose.tools import *
import networkx_v1 as nx
import networkx_v1.algorithms.approximation as a

def test_independent_set():
    # smoke test
    G = nx.Graph()
    assert_equal(len(a.maximum_independent_set(G)),0)
