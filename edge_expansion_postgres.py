import heapq
from collections import namedtuple
from recordtype import recordtype
from pprint import pprint

from utils import get_node_edges, get_edge_by_id


def edge_expansion(edge, threshold, cursor):
  EDC = []

  # added for avoid move back in network during searching
  visited_edges = [edge.edge_id]

  for node_geom in [edge.start_node, edge.end_node]:
    # for n in NODES:
    #   n['dis'] = 0
    visited_nodes = []

    # TODO: maybe it should be copy of this node
    Node = recordtype('Node', 'geom dis')
    node = Node(node_geom, 0)
    H = []
    heapq.heappush(H, (node.dis, node))

    while H:
      node_min = heapq.heappop(H)[1]
      visited_nodes.append(node_min.geom)

      for edge_prim_record in get_node_edges(node_min.geom, cursor):
        edge_prim_id = edge_prim_record.edge_id

        if not edge_prim_id in visited_edges:
          edge_prim = get_edge_by_id(edge_prim_id, cursor)
          visited_edges.append(edge_prim_id)

          if node_geom == edge.start_node and node_min.geom == edge_prim.start_node:
            EDC.append((edge.edge_id, edge_prim.edge_id, 'SS', node_min.dis))
            other_edge_prim_node = Node(edge_prim.end_node, 0)

          if node_geom == edge.start_node and node_min.geom == edge_prim.end_node:
            EDC.append((edge.edge_id, edge_prim.edge_id, 'SE', node_min.dis))
            other_edge_prim_node = Node(edge_prim.start_node, 0)

          if node_geom == edge.end_node and node_min.geom == edge_prim.start_node:
            EDC.append((edge.edge_id, edge_prim.edge_id, 'ES', node_min.dis))
            other_edge_prim_node = Node(edge_prim.end_node, 0)

          if node_geom == edge.end_node and node_min.geom == edge_prim.end_node:
            EDC.append((edge.edge_id, edge_prim.edge_id, 'EE', node_min.dis))
            other_edge_prim_node = Node(edge_prim.start_node, 0)
          
          # find other node_primes of edge_prime
          if other_edge_prim_node.geom not in visited_nodes:
              # other_edge_prim_node['dis'] > node_min['dis'] + edge_prim['weight'] omitted
              if threshold >= node_min.dis + edge_prim.weight:
                other_edge_prim_node.dis = node_min.dis + edge_prim.weight
                heapq.heappush(H, (other_edge_prim_node.dis, other_edge_prim_node))

  return EDC
