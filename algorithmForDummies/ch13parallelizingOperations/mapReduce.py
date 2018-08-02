L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
m = list(map(lambda x: x ** 2, L))
print(m)

from functools import reduce

r = reduce(lambda x, y: x + y, m)
print(r)

import urllib.request

url = 'http://gutenberg.readingroo.ms/2/6/0/2600/2600.txt'
response = urllib.request.urlopen(url)
data = response.read()
text = data.decode('utf-8')[627:]

print(text[:37])

words = text.split()
print('Number of words: %i' % len(words))
