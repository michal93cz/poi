from edge_expansion import edge_expansion
from neighbor_objects_refining import neighbor_objects_refining

# N = 'set of nodes'
# E = 'set of edges'
# G = (N, E)

# O = 'set of objects'
# Oe = 'set of objects snappet to edge e'
# oi = ('nearest edge', 'distance from start node')

# d = 'threshold distance' 
# node = ('set of adjacent egdes')
# edge = ('start node', 'end node', 'edge weight', 'objects snappet to the edge (are very close the edge)')

object1 = { 'id': 'object1', 'edge': 'edge1', 'distance': 3 }
object2 = { 'id': 'object2', 'edge': 'edge2', 'distance': 2 }
object3 = { 'id': 'object3', 'edge': 'edge3', 'distance': 4 }
object4 = { 'id': 'object4', 'edge': 'edge4', 'distance': 6 }

node1 = { 'id': 'node1', 'edges': ['edge1'] }
node2 = { 'id': 'node2', 'edges': ['edge1', 'edge2'] }
node3 = { 'id': 'node3', 'edges': ['edge2', 'edge3'] }
node4 = { 'id': 'node4', 'edges': ['edge3'] }

edge1 = { 'id': 'edge1', 'nodes': [node1, node2], 'weight': 5, 'objects': [object1, object2] }
edge2 = { 'id': 'edge2', 'nodes': [node2, node3], 'weight': 7, 'objects': [object3] }
edge3 = { 'id': 'edge3', 'nodes': [node3, node4], 'weight': 10, 'objects': [object4] }

edges = [edge1, edge2, edge3]
nodes = [node1, node2, node3, node4]
objects = [object1, object2, object3, object4]
threshold = 5

def ens(edges, threshold):
  st = []
  for edge in edges:
    edc = edge_expansion(edge, threshold, edges)

    for item in edc:
      stc = neighbor_objects_refining(item, threshold)
      st.append(stc)

  return st

ens(edges, threshold)
