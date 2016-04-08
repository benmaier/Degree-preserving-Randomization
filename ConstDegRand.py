import numpy as np
import random 
from collections import Counter

def degree_preserving_randomization(edges_):
    
    edges = set( [tuple(e) for e in edges_ ]) 
    stubs = [ ]
    [ stubs.extend(e) for e in edges ]
    stubs = stubs
    stub_counter = Counter(stubs)

    done = False
    new_edges = set()
    while not done:

        # available_nodes
        nodes = np.array([ stub for stub,count in stub_counter.iteritems() if count!=0 ])
            
        if len(nodes)==0:
            done = True
            break

        first,second = -1,-1
        while first == second and len(nodes)>1:
            first,second = np.random.choice(nodes,size=(2,),replace=False)

        if first!=second and \
           (first,second) not in new_edges and \
           (second,first) not in new_edges and \
           len(nodes)>1:
            new_edges.add((first,second))
            stub_counter[first] -= 1
            stub_counter[second] -= 1
        else:
            #pop a random edge and put its nodes back in the stub pool
            edge = random.sample(new_edges,1)[0]
            new_edges.remove(edge)
            stub_counter[edge[0]] += 1
            stub_counter[edge[1]] += 1
        
    return new_edges

