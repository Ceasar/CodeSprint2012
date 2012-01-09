import itertools


def get_input():
  import sys
  n = None
  for i, line in enumerate(sys.stdin.xreadlines()):
    if i != 0:
      if i % 2 == 0:
        cards = [int(i) for i in line.strip().split()]
        yield n, cards
      else:
        n = int(line.strip())


if __name__ == "__main__":
  for _, cards in get_input():
    count = 0
    for permutation in itertools.permutations(indices):
      for i, j in enumerate(permutation):
        if cards[j] > i:
          break
      else:
        count += 1
    print count
