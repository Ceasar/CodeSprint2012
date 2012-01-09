

def get_input(input_):
  n, q = input_.next().strip().split()
  n, q = int(n), int(q)
  points =[]
  polygons = []

  for _ in range(n):
    x, y = input_.next().strip().split()
    points.append((int(x), int(y)))
  assert len(points) == n
  
  polygon = []
  for line in input_:
    tokens = line.strip().split()
    if len(tokens) == 1:
      if polygon:
        assert len(polygon) == m
        polygons.append(polygon)
      polygon = []
      m = int(tokens[0])
    elif len(tokens) == 2:
      x, y = tokens
      polygon.append((int(x), int(y)))
  polygons.append(polygon)

  assert len(polygons) == q
  return points, polygons


def in_poly(poly, point):
  if any(vertex == point for vertex in poly):
    return True

  result = False
  x, y = point
  p1x, p1y = poly[-1]
  for vertex in poly:
    p2x, p2y = vertex
    if max(p1y, p2y) >= y >= min(p1y, p2y):
      if p1y == p2y:
        if max(p1x, p2x) >= x >= min(p1x, p2x):
          return True
      else:
        xintersect = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
        if max(p1x, p2x) > x and xintersect > x:
          result = not result
        elif xintersect == x:
          return True
    p1x, p1y = p2x, p2y
  return result

if __name__ == "__main__":
  import sys
  points, polygons = get_input(sys.stdin.xreadlines())
  out = []
  for polygon in polygons:
    out.append(str(sum(in_poly(polygon, point) for point in points)))
  print "\n".join(out)
