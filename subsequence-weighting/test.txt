
def max_subarray(li):
  """Find the contiguous subarray within a list which has the largest sum.
  >>> li = [-2, 1, 1, -3, 2, 1, -1, 4, -5, 4]
  >>> max_subarray(li)
  6
  """
  max_so_far = max_ending_here = 0
  for e in li:
    max_ending_here = max(0, max_ending_here + e)
    max_so_far = max(max_so_far, max_ending_here)
  return max_so_far

if __name__ == "__main__":
  import doctest
  doctest.testmod()
