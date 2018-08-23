from edge_expansion import edge_expansion
from neighbor_objects_refining import neighbor_objects_refining

object1 = ('')

node1 = ('node1', ['edge1', 'edge2'])
node2 = ('node2', ['edge2', 'edge3'])
node3 = ('node3', ['edge3', 'edge4'])
node4 = ('node4', ['edge1', 'edge4'])

edge1 = ('edge1', node1, node4, 5)

def ens(edges, threshold):
  st = []
  for edge in edges:
    edc = []
    edc = edge_expansion(edge, threshold)

    for item in edc:
      stc = []
      stc = neighbor_objects_refining(item, threshold)

      st.append(stc)

  return st
# N = 'set of nodes'
# E = 'set of edges'
# G = (N, E)

# O = 'set of objects'
# Oe = 'set of objects snappet to edge e'
# oi = ('nearest edge', 'distance from start node')

# d = 'threshold distance' 
# node = ('set of adjacent egdes')
# edge = ('start node', 'end node', 'edge weight', 'objects snappet to the edge (are very close the edge)')


ens([4, 5], 6)
