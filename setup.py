#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup script for networkx_v1

You can install networkx_v1 with

python setup.py install
"""
from glob import glob
import os
import sys
if os.path.exists('MANIFEST'):
    os.remove('MANIFEST')

from setuptools import setup

if sys.argv[-1] == 'setup.py':
    print("To install, run 'python setup.py install'")
    print()

if sys.version_info[:2] < (2, 7):
    print("NetworkX requires Python 2.7 or later (%d.%d detected)." %
          sys.version_info[:2])
    sys.exit(-1)

# Write the version information.
sys.path.insert(0, 'networkx_v1')
import release
version = release.write_versionfile()
sys.path.pop(0)

packages=["networkx_v1",
          "networkx_v1.algorithms",
          "networkx_v1.algorithms.assortativity",
          "networkx_v1.algorithms.bipartite",
          "networkx_v1.algorithms.centrality",
          "networkx_v1.algorithms.chordal",
          "networkx_v1.algorithms.community",
          "networkx_v1.algorithms.components",
          "networkx_v1.algorithms.connectivity",
          "networkx_v1.algorithms.coloring",
          "networkx_v1.algorithms.flow",
          "networkx_v1.algorithms.traversal",
          "networkx_v1.algorithms.isomorphism",
          "networkx_v1.algorithms.shortest_paths",
          "networkx_v1.algorithms.link_analysis",
          "networkx_v1.algorithms.operators",
          "networkx_v1.algorithms.approximation",
          "networkx_v1.algorithms.tree",
          "networkx_v1.classes",
          "networkx_v1.external",
          "networkx_v1.generators",
          "networkx_v1.drawing",
          "networkx_v1.linalg",
          "networkx_v1.readwrite",
          "networkx_v1.readwrite.json_graph",
          "networkx_v1.tests",
          "networkx_v1.testing",
          "networkx_v1.utils"]

docdirbase  = 'share/doc/networkx_v1-%s' % version
# add basic documentation
data = [(docdirbase, glob("*.txt"))]
# add examples
for d in ['advanced',
          'algorithms',
          'basic',
          '3d_drawing',
          'drawing',
          'graph',
          'multigraph',
          'pygraphviz',
          'readwrite']:
    dd = os.path.join(docdirbase,'examples', d)
    pp = os.path.join('examples', d)
    data.append((dd, glob(os.path.join(pp ,"*.py"))))
    data.append((dd, glob(os.path.join(pp ,"*.bz2"))))
    data.append((dd, glob(os.path.join(pp ,"*.gz"))))
    data.append((dd, glob(os.path.join(pp ,"*.mbox"))))
    data.append((dd, glob(os.path.join(pp ,"*.edgelist"))))

# add the tests
package_data     = {
    'networkx_v1': ['tests/*.py'],
    'networkx_v1.algorithms': ['tests/*.py'],
    'networkx_v1.algorithms.assortativity': ['tests/*.py'],
    'networkx_v1.algorithms.bipartite': ['tests/*.py'],
    'networkx_v1.algorithms.centrality': ['tests/*.py'],
    'networkx_v1.algorithms.chordal': ['tests/*.py'],
    'networkx_v1.algorithms.community': ['tests/*.py'],
    'networkx_v1.algorithms.components': ['tests/*.py'],
    'networkx_v1.algorithms.connectivity': ['tests/*.py'],
    'networkx_v1.algorithms.coloring': ['tests/*.py'],
    'networkx_v1.algorithms.flow': ['tests/*.py', 'tests/*.bz2'],
    'networkx_v1.algorithms.traversal': ['tests/*.py'],
    'networkx_v1.algorithms.isomorphism': ['tests/*.py','tests/*.*99'],
    'networkx_v1.algorithms.link_analysis': ['tests/*.py'],
    'networkx_v1.algorithms.approximation': ['tests/*.py'],
    'networkx_v1.algorithms.operators': ['tests/*.py'],
    'networkx_v1.algorithms.shortest_paths': ['tests/*.py'],
    'networkx_v1.algorithms.traversal': ['tests/*.py'],
    'networkx_v1.algorithms.tree': ['tests/*.py'],
    'networkx_v1.classes': ['tests/*.py'],
    'networkx_v1.generators': ['tests/*.py'],
    'networkx_v1.drawing': ['tests/*.py'],
    'networkx_v1.linalg': ['tests/*.py'],
    'networkx_v1.readwrite': ['tests/*.py'],
    'networkx_v1.readwrite.json_graph': ['tests/*.py'],
    'networkx_v1.testing': ['tests/*.py'],
    'networkx_v1.utils': ['tests/*.py']
    }

install_requires = ['decorator>=3.4.0']

if __name__ == "__main__":

    setup(
        name             = release.name.lower(),
        version          = version,
        maintainer       = release.maintainer,
        maintainer_email = release.maintainer_email,
        author           = release.authors['Hagberg'][0],
        author_email     = release.authors['Hagberg'][1],
        description      = release.description,
        keywords         = release.keywords,
        long_description = release.long_description,
        license          = release.license,
        platforms        = release.platforms,
        url              = release.url,
        download_url     = release.download_url,
        classifiers      = release.classifiers,
        packages         = packages,
        data_files       = data,
        package_data     = package_data,
        install_requires = install_requires,
        test_suite       = 'nose.collector',
        tests_require    = ['nose>=0.10.1'],
        zip_safe         = False
    )
