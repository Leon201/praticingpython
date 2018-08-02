hash_functions = 3
bit_vector_length = 10
bit_vector = [0] * bit_vector_length

from hashlib import md5, sha1

def hash_f(element, i , length):
    """ This is a magic function """
    h1 = int(md5(element.encode('ascii')).hexdigest(), 16)
    h2 = int(sha1(element.encode('ascii')).hexdigest(), 16)
    return (h1 + i * h2) % length

def insert_filter(website):
    result = list()
    for hash_number in range(hash_functions):
        position = hash_f(website, hash_number, bit_vector_length)
        result.append(position)
        bit_vector[position] = 1
    print ('Inserted in positions: %s' % result)

def check_filter(website):
    result = list()
    for hash_number in range(hash_functions):
        position = hash_f(website, hash_number, bit_vector_length)
        result.append((position, bit_vector[position]))
    print ('Bytes in positions: %s' % result)

insert_filter('wikipedia.org')
print(bit_vector)
insert_filter('youtube.com')

check_filter('yahoo.com')

# 把vector变成1，是想干什么嫩，三种hash的位置，对饮位置的bit_vector
# 后面就没有代码的，然后说了一下，hash值永远是会发生冲突的
