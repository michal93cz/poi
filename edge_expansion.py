import heapq
from pprint import pprint

from utils import search_in_array_of_dicts


def edge_expansion(edge, threshold, EDGES):
  EDC = []

  for node in edge['nodes']:
    # TODO: maybe it should be copy of this node
    node['dis'] = 0
    H = []
    heapq.heappush(H, node) # TODO: add custom key

    while H:
      node_min = heapq.heappop(H)
      node_min['visited'] = True

      for edge_prim_name in node_min['edges']:
        edge_prim = search_in_array_of_dicts(EDGES, 'id', edge_prim_name)
        if not edge_prim is edge:
          if node is edge['nodes'][0] and node_min is edge_prim['nodes'][0]:
            EDC.append((edge, edge_prim, 'SS', node_min['dis']))
            other_edge_prim_node = edge_prim['nodes'][1]

          if node is edge['nodes'][0] and node_min is edge_prim['nodes'][1]:
            EDC.append((edge, edge_prim, 'SE', node_min['dis']))
            other_edge_prim_node = edge_prim['nodes'][0]

          if node is edge['nodes'][1] and node_min is edge_prim['nodes'][0]:
            EDC.append((edge, edge_prim, 'ES', node_min['dis']))
            other_edge_prim_node = edge_prim['nodes'][1]

          if node is edge['nodes'][1] and node_min is edge_prim['nodes'][1]:
            EDC.append((edge, edge_prim, 'EE', node_min['dis']))
            other_edge_prim_node = edge_prim['nodes'][0]

          # find other node_primes of edge_prime
          if not 'visited' in other_edge_prim_node:
            # other_edge_prim_node['dis'] > node_min['dis'] omitted because other not always doesn't have 'dis' field yet
            if threshold >= node_min['dis'] + edge_prim['weight']:
              other_edge_prim_node['dis'] = node_min['dis'] + edge_prim['weight']
              heapq.heappush(H, other_edge_prim_node)

  return EDC
