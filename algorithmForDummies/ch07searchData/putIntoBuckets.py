data = [22, 40, 102, 105, 23, 31, 6, 5]

hash_table = [None] * 15
# 元素乘以15，是代表一维数组然后容量是15，吧

tblLen = len(hash_table)

# 哈希值的函数，直接用值除以哈希表的大小
def hash_function(value, table_size):
    return value % table_size

for value in data:
    hash_table[hash_function(value, tblLen)] = value

print(hash_table)

# 哈希表也是普通功德数组