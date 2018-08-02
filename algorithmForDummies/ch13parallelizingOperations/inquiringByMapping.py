import os

if os.name == "nt":
    from multiprocessing.dummy import Pool
else:
    from multiprocessing import Pool

from multiprocessing import cpu_count
from functools import partial


def remove_punctuation(text):
    return ''.join([l for l in text if l not in ['.', ',', '!', '?', '"']])


def count_words(list_of_words, keywordss):
    results = list()
    for word in list_of_words:
        for keyword in keywordss:
            if keyword.upper() == remove_punctuation(word.upper()):
                results.append((keyword, 1))
    return results


def Partition(data, size):
    return [data[x: x + size] for x in range(0, len(data), size)]


def Distribute(function, data, cores):
    pool = Pool(cores)
    results = pool.map(function, data)
    pool.close()
    return results


def Shuffle_Sort(L):
    Mapping = dict()
    for sublist in L:
        for key_pair in sublist:
            key, value = key_pair
            if key in Mapping:
                Mapping[key].append(key_pair)
            else:
                Mapping[key] = [key_pair]
    return [Mapping[key] for key in Mapping]


def Reduce(Mapping):
    return (Mapping[0][0], sum([value for (key, value) in Mapping]))


# ---------
n = cpu_count()
print('Yout have %i cores available for MapReduce' % n)

# Map = (count_words, ['WAR' 'PEACE', 'RUSSIA', 'NAPOLEAN'])
# 这里有一点不理解的就是，除了函数名称，这里的参数是一个字典，那后面map的时候, 怎么就把这个字典（数组）放到了第二个参数上面
# 是不是这个方法只有两个参数的时候，这里的keywords就自动放在了第二个入参的位置
# 那我这里尝试传入多个参数，看一下测试的结果
# 前面就因为少了一个逗号，然后因为Napoleon一直找不出来所以shuffle就无法理解结果
# 这里的partial就是一个map对象，但是这个map又是一个封装了的对象，然后map函数的第一个参数是可以传入的
# 这里的map函数也不是自定义的，是多进程模块中的pool的map
Map = partial(count_words, keywordss=['WAR', 'PEACE', 'RUSSIA', 'NAPOLEON'])
# Map = partial(count_words, keywords=['WAR', 'PEACE', 'RUSSIA', 'NAPOLEAN'])
print(Map)

from algorithmForDummies.ch13parallelizingOperations.mapReduce import words

print(len(words) // n + 1)
print(len(words) // (n + 1))
map_result = Distribute(Map, Partition(words, len(words) // n + 1), n)

print('map_result is a list made of %i elements' % len(map_result))

print('Preview of one element: %s' % map_result[0][:5])

Shuffled = Shuffle_Sort(map_result)

print('Shuffled is a list made of %i elements' % len(Shuffled))

print('Preview of first element: %s]' % Shuffled[0][:5])
# print( Shuffled)
# print( map_result)
print('Preview of second element: %s]' % Shuffled[1][:5])

result = Distribute(Reduce, Shuffled, n)
print('Emitted results are: %s' % result)

import urllib.request

url = "http://gutenberg.pglaf.org/1/6/6/1661/1661.txt"
text = urllib.request.urlopen(url).read().decode('utf-8')[723:]

words = text.split()

print(text[:65])
print('\nTotal words are %i' % len(words))
Map = partial(count_words, keywordss=['WATSON', 'ELEMENTARY'])
result = Distribute(Reduce
                    , Shuffle_Sort(
        Distribute(Map
                   , Partition(words, len(words) // n)
                   , n)
    )
                    , 1)
print('Emitted results are: %s' % result)
