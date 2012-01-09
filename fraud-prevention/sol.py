
KEYS = ['orderid', 'dealid', 'email', 'address', 'city', 'state', 'zip', \
    'creditcard']

def normalize_email(email):
  # lower
  email = email.lower()
  name, domain = email.split('@') #assumes one
  # remove periods
  name = "".join(name.split('.'))
  # remove +
  name = name.split('+')[0]
  email = "@".join([name, domain])
  return email


def normalize_address(address):
  # lower
  address = address.lower()
  # expand street
  address = address.replace("st.", "street")
  address = address.replace("rd.", "road")
  return address

def normalize(record):
  # normalize email
  record['email'] = normalize_email(record['email'])

  # normalize address
  record['address'] = normalize_address(record['address'])

  # normalize city
  city = record['city']
  # lower
  city = city.lower()
  record['city'] = city

  # normalize state
  state = record['state']
  # lower
  state = state.lower()
  # expand state
  state = state.replace("california", "ca")
  state = state.replace("illinois", "il")
  state = state.replace("new york", "ny")
  record['state'] = state

def get_input(input_):
  records = []
  for i, line in enumerate(input_): 
    if i == 0:
      n = int(line.strip())
    else:
      values = line.strip().split(',')
      record = dict(zip(KEYS, values))
      normalize(record)
      records.append(record)
  return n, records


def get_frauds(records):
  """Takes a set of records with the same deal id.
  Returns a set of fraudelent order ids."""
  result = set()

  emails = {} # email -> record
  # Get email result
  for record in records:
    email = record['email']
    if email not in emails:
      emails[email] = record
    else:
      if record['creditcard'] != emails[email]['creditcard']:
        result.add(emails[email]['orderid'])
        result.add(record['orderid'])

  addresses = {} # address -> record
  # Get address result
  for record in records:
    address = record['address'], record['zip'], record['city'], record['state']
    if address not in addresses:
      addresses[address] = record
    else:
      if record['creditcard'] != addresses[address]['creditcard']:
        result.add(addresses[address]['orderid'])
        result.add(record['orderid'])

  return result


if __name__ == "__main__":
  from collections import defaultdict
  import sys
  n, records = get_input(sys.stdin.xreadlines())

  # group by deals
  deals = defaultdict(list) # dealid -> list[RECORD]
  for record in records:
    deals[record['dealid']].append(record)

  # find frauds
  frauds = set()
  for deal in deals:
    frauds.update(get_frauds(deals[deal]))

  # return result
  result = [int(s) for s in frauds]
  result.sort()
  print ",".join([str(i) for i in result])

