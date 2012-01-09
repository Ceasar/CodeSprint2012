from fractions import Fraction

def get_input(input_):
  for i, line in enumerate(input_):
    if i == 0:
      continue
    else:
      n, m = line.strip().split()
      yield int(n), int(m)

def exp(n, p):
  return ((p ** -n) - 1) / (1 - p)

def solve(n, m):
  return -2 * (2 ** m - 2 ** n)

if __name__ == "__main__":
  import sys
  for case in get_input(sys.stdin.xreadlines()):
    n, m = case
    assert 1000 >= n >= m >= 0, "%s %s" % (n, m)
    # print "%.2f" % (exp(n, 0.5) - exp(m, 0.5))
    print "%.2f" % (solve(n, m))
