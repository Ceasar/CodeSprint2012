

def get_input(input_):
  n, v = None, []
  for i, line in enumerate(input_):
    if i > 0:
      row = tuple(int(i) for i in line.strip().split())
      assert len(row) == n
      v.append(row)
    else:
      n = int(line)
      assert n <= 50
  assert len(v) == n
  return n, tuple(v)

def chunk(li, n):
  for i, e in enumerate(li):
    try:
      pair = li[i:i+n] 
      assert len(pair) == n
      yield pair
    except:
      break

def memoize(func):
  mem = {}
  def memoized(*args):
    try:
      return mem[args]
    except KeyError:
      result = mem[args] = func(*args)
      return result
  return memoized

@memoize
def score(permutation, v):
  if len(permutation) < 2:
    return 0
  if len(permutation) == 2:
    y, x = permutation
    return v[y][x]
  else:
    n = len(permutation) / 2
    y, x = permutation[n-1], permutation[n]
    return v[y][x] + score(permutation[:n], v) + score(permutation[n:], v)

if __name__ == "__main__":
  import itertools
  import sys
  n, v = get_input(sys.stdin.xreadlines())
  permutations = itertools.permutations(xrange(n))
  def V(permutation):
    return score(permutation, v)
  result = max(permutations, key=V)
  print " ".join([str(r) for r in result])
