import itertools


def get_input(input_):
  sequence = []
  for i, line in enumerate(input_):
    if i == 0 or i % 3 == 1:
      continue
    if i % 3 == 2:
      sequence = [int(s) for s in line.strip().split()]
    else:
      weights = [int(w) for w in line.strip().split()]
      assert len(sequence) == len(weights)
      yield itertools.izip(sequence, weights)


if __name__ == "__main__":
  import sys
  for sequence in get_input(sys.stdin.xreadlines()):
    best = {}
    for num, weight in sequence:
      for key in best.keys():
        if key[-1] < num:
          new_key = key + (num,)
          new_weight = best[key] + weight
          if new_key not in best or best[new_key] < new_weight:
            best[new_key] = new_weight
          
      if num not in best or best[num] < weight:
        best[(num,)] = weight

    result = max(best.values())
    print result

    del best, num, weight, key
