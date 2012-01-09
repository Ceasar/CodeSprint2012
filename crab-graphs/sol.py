
def get_input(input_):
  ncases = int(input_.next())

  nodes = set()
  edges = set()
  for i, line in enumerate(input_):
    tokens = [int(token) for token in line.strip().split()]
    if len(tokens) == 3:
      if i != 0:
        yield nodes, t, edges
      n, t, m = tokens
    else:
      u, v = tokens
      nodes.add(u)
      nodes.add(v)
      edges.add((u, v))
  yield nodes, t, edges

if __name__ == "__main__":
  import sys
  for nodes, t, edges in get_input(sys.stdin.xreadlines()):
    graph = {}
    for edge in edges:
      u, v = edge
      graph[u].append(v)
      graph[v].append(u)
    covered = set()

