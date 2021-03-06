import heapq
from pprint import pprint

from utils import search_in_array_of_dicts


def edge_expansion(edge, threshold, EDGES, NODES):
  EDC = []

  # added for avoid move back in network during searching
  visited_edges = [edge['id']]

  for node in edge['nodes']:
    for n in NODES:
      n['dis'] = 0

    # TODO: maybe it should be copy of this node
    node['dis'] = 0
    H = []
    heapq.heappush(H, (node['dis'], node))

    while H:
      node_min = heapq.heappop(H)[1]
      node_min['visited'] = True

      for edge_prim_name in node_min['edges']:
        if not edge_prim_name in visited_edges:
          edge_prim = search_in_array_of_dicts(EDGES, 'id', edge_prim_name)
          visited_edges.append(edge_prim_name)

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

          # print('Edge:', edge['id'], '  Node:', node['id'], '  Node_min:', node_min['id'], '  E_prim:', edge_prim_name, '  Other:', other_edge_prim_node['id'])
          
          # find other node_primes of edge_prime
          if 'visited' in other_edge_prim_node and not other_edge_prim_node['visited'] or not 'visited' in other_edge_prim_node:
              # other_edge_prim_node['dis'] > node_min['dis'] + edge_prim['weight'] omitted
              if threshold >= node_min['dis'] + edge_prim['weight']:
                other_edge_prim_node['dis'] = node_min['dis'] + edge_prim['weight']
                heapq.heappush(H, (other_edge_prim_node['dis'], other_edge_prim_node))

  return EDC
