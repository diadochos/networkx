"""
NetworkX
========

    NetworkX (NX) is a Python package for the creation, manipulation, and
    study of the structure, dynamics, and functions of complex networks.

    https://networkx.lanl.gov/

Using
-----

    Just write in Python

    >>> import networkx_v1 as nx
    >>> G=nx.Graph()
    >>> G.add_edge(1,2)
    >>> G.add_node(42)
    >>> print(sorted(G.nodes()))
    [1, 2, 42]
    >>> print(sorted(G.edges()))
    [(1, 2)]
"""
#    Copyright (C) 2004-2015 by
#    Aric Hagberg <hagberg@lanl.gov>
#    Dan Schult <dschult@colgate.edu>
#    Pieter Swart <swart@lanl.gov>
#    All rights reserved.
#    BSD license.
#
# Add platform dependent shared library path to sys.path
#

from __future__ import absolute_import

import sys
if sys.version_info[:2] < (2, 7):
    m = "Python 2.7 or later is required for NetworkX (%d.%d detected)."
    raise ImportError(m % sys.version_info[:2])
del sys

# Release data
from networkx_v1 import release

__author__ = '%s <%s>\n%s <%s>\n%s <%s>' % \
    (release.authors['Hagberg'] + release.authors['Schult'] +
        release.authors['Swart'])
__license__ = release.license

__date__ = release.date
__version__ = release.version

__bibtex__ = """@inproceedings{hagberg-2008-exploring,
author = {Aric A. Hagberg and Daniel A. Schult and Pieter J. Swart},
title = {Exploring network structure, dynamics, and function using {NetworkX}},
year = {2008},
month = Aug,
urlpdf = {http://math.lanl.gov/~hagberg/Papers/hagberg-2008-exploring.pdf},
booktitle = {Proceedings of the 7th Python in Science Conference (SciPy2008)},
editors = {G\"{a}el Varoquaux, Travis Vaught, and Jarrod Millman},
address = {Pasadena, CA USA},
pages = {11--15}
}"""

# These are import orderwise
from networkx_v1.exception import *
import networkx_v1.external
import networkx_v1.utils

import networkx_v1.classes
from networkx_v1.classes import *


import networkx_v1.convert
from networkx_v1.convert import *

import networkx_v1.convert_matrix
from networkx_v1.convert_matrix import *


import networkx_v1.relabel
from networkx_v1.relabel import *

import networkx_v1.generators
from networkx_v1.generators import *

import networkx_v1.readwrite
from networkx_v1.readwrite import *

# Need to test with SciPy, when available
import networkx_v1.algorithms
from networkx_v1.algorithms import *
import networkx_v1.linalg

from networkx_v1.linalg import *
from networkx_v1.tests.test import run as test

import networkx_v1.drawing
from networkx_v1.drawing import *
