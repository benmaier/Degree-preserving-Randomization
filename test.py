import networkx as nx
import numpy as np
import random 
import csv
import pylab as pl
from collections import Counter

from networkprops import networkprops as nprops

from ConstDegRand import degree_preserving_randomization

G = nx.fast_gnp_random_graph(100,0.1)
edges = G.edges()
nodes = G.nodes()

edges = []
nodes = set()
with open("list.csv","r") as csvfile:
    reader = csv.reader(csvfile,delimiter=' ')
   
    next(reader,None)
    for row in reader:
        edge = row[:2]
        edges.append(edge)

G = nx.Graph()

G.add_edges_from(edges)

 
new_edges = degree_preserving_randomization(edges)

G2 = nx.Graph()
G2.add_edges_from(new_edges)

nprops1 = nprops(G)
ks1,vals1 = nprops1.get_degree_distribution()

nprops2 = nprops(G2)
ks2,vals2 = nprops2.get_degree_distribution()

pl.plot(ks1,vals1)
pl.plot(ks2,vals2)

fig,ax = pl.subplots(1,2)
nx.draw(G,ax=ax[0])
nx.draw(G2,ax=ax[1])

print len(edges), len(new_edges)
print "no self-links:", all( [ e[0]!=e[1] for e in new_edges] ) 

pl.show()

