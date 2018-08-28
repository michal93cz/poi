from pprint import pprint

from edge_expansion import edge_expansion
from neighbor_objects_refining import neighbor_objects_refining
from prepared_data import edges

threshold = 20

def ens(edges, threshold):
  ST = []

  for edge in edges:
    EDC = edge_expansion(edge, threshold, edges)

    for tuple in EDC:
      if tuple[3] <= threshold:
        STC = neighbor_objects_refining(tuple, threshold)
        ST.append(STC)

  return ST

pprint(ens(edges, threshold))
