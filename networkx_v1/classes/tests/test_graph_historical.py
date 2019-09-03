#!/usr/bin/env python
"""Original NetworkX graph tests"""
from nose.tools import *
import networkx_v1
import networkx_v1 as nx

from historical_tests import HistoricalTests

class TestGraphHistorical(HistoricalTests):

    def setUp(self):
        HistoricalTests.setUp(self)
        self.G=nx.Graph

