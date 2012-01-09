
def get_input(input_):
  t, q, n = input_.next().strip().split()
  t, q, n = int(t), int(q), int(n)

  topics = []
  tids = set()
  for _ in range(t):
    tid, x, y = input_.next().strip().split()
    topics.append((int(tid), float(x), float(y)))
    tids.add(tid)
  assert len(topics) == len(tids) == t

  questions = []
  for _ in range(q):
    line = input_.next().strip().split()
    qid, ntids, tids_ = int(line[0]), int(line[1]), set(int(s) for s in line[2:] if s in tids)
    assert all(str(tid) in tids for tid in tids_), "%s %s" % (tids, tids_)
    assert len(tids_) == ntids, "%s: %s %s" % (qid, tids_, ntids)
    # don't append question if it doesn't have any topics
    if ntids > 0:
      questions.append((qid, ntids, tids_))
  assert len(questions) <= q

  queries = []
  for _ in range(n):
    q, r, x, y = input_.next().strip().split()
    queries.append((q, int(r), float(x), float(y)))
  assert len(queries) == n

  return topics, questions, queries


def distance(x, y, x2, y2):
  '''Sort by distance, then by id.'''
  result = ((x - x2) ** 2 + (y - y2) ** 2) ** 0.5
  assert result >= 0
  return result


def get_distances(topics):
  distances = {}
  for topic in topics:
    tid, x2, y2 = topic
    distances[tid] = distance(x, y, x2, y2)
  return distances


if __name__ == "__main__":
  import sys
  topics, questions, queries = get_input(sys.stdin.xreadlines())
  for query in queries:
    q, r, x, y = query

    distances = get_distances(topics)

    if q == 'q':
      """
      Distance of a question from a point is the minimum of the distance
      of all topics associated with that question.
      """
      def qsorter(question):
        qid, _, tids = question
        return min((distances[tid], -qid) for tid in tids)
      questions.sort(key=qsorter)
      print " ".join([str(question[0]) for question in questions[:r]])
    elif q == 't':
      def tsorter(topic):
        tid, _, _ = topic
        return distances[tid], -tid
      topics.sort(key=tsorter)
      print " ".join([str(topic[0]) for topic in topics[:r]])
    else:
      raise ValueError()
