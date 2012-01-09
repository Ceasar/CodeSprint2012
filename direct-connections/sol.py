import itertools

def get_input(input_):
  distances = []
  for i, line in enumerate(input_):
    if i == 0 or i % 3 == 1:
      continue
    elif i % 3 == 2:
      distances = [int(d) for d in line.strip().split()]
    else:
      people = [int(p) for p in line.strip().split()]
      yield zip(distances, people)

if __name__ == "__main__":
  import sys
  for cities in get_input(sys.stdin.xreadlines()):
    cable = 0
    for i, city in enumerate(cities):
      dist1, pop1 = city
      for j in xrange(i+1, len(cities)):
        dist2, pop2 = cities[j]
        cable += abs(dist1 - dist2) * max(pop1, pop2)
        cable %= 1000000007
    print cable
