import heapq


def edge_expansion(edge, threshold):
  # edge has nodes
  for node in edge:
    H = []
    heapq.heappush(H, node)

    while H:
      n = heapq.heappop(heap)

      for e in n:
        if e is "start_node":
          EDC.insert(edge, e, SS, n[dis])

  print(edge, threshold)

  return [edge, threshold]
