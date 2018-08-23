import heapq


def edge_expansion(edge, threshold, EDGES):
  for node in edge['nodes']:
    # maybe it should be copy of this node
    node['dist'] = 0
    H = []
    heapq.heappush(H, node)

    while H:
      node_min = heapq.heappop(H)
      node_min['visited'] = True

      EDC = []
      for edge_prim_name in node_min['edges']:
        edge_prim = search_in_array_of_dicts(EDGES, 'id', edge_prim_name)
        
        if node is edge['nodes'][0] and node_min is edge_prim['nodes'][0]:
          EDC.append((edge, edge_prim, 'SS', node_min['dist']))

        if node is edge['nodes'][0] and node_min is edge_prim['nodes'][1]:
          EDC.append((edge, edge_prim, 'SE', node_min['dist']))

        if node is edge['nodes'][1] and node_min is edge_prim['nodes'][0]:
          EDC.append((edge, edge_prim, 'ES', node_min['dist']))

        if node is edge['nodes'][0] and node_min is edge_prim['nodes'][1]:
          EDC.append((edge, edge_prim, 'EE', node_min['dist']))

        # find other node_primes of edge_prime

  return EDC

def search_in_array_of_dicts(array, key, value):
  for item in array:
    if item[key] == value:
      return item
