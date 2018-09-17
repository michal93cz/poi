from pprint import pprint

from edge_expansion import edge_expansion
from neighbor_objects_refining import neighbor_objects_refining
from prepared_data import edges, nodes

threshold = 20

def ens(edges, threshold, nodes):
  ST = []

  for edge in edges:
    EDC = edge_expansion(edge, threshold, edges, nodes)

    for tuple in EDC:
      print(tuple[0]['id'], tuple[1]['id'], tuple[2], tuple[3])

      if tuple[3] <= threshold:
        STC = neighbor_objects_refining(tuple, threshold)
        # pprint(STC)
        ST.append(STC)

  return ST

pprint(ens(edges, threshold, nodes))
# ens(edges, threshold, nodes)
