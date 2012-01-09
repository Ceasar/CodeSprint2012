

def get_input(input_):
  for i, line in enumerate(input_):
    if i > 0:
      expr, l = line.strip().split()
      yield expr, l


if __name__ == "__main__":
  import sys
  for expr, l in get_input(sys.stdin.xreadlines()):
    items = []
    operators = []
    for char in expression:
      if char in ("*", "|"):
        operators.append(char)
      else:
        items.append(char)
    
    while len(operators) > 0:
      op = operators.pop()
      if op == "*":
        



