from bintrees import BinaryTree

data = {3: 'White', 2: 'Red', 1: 'Green', 5: 'Orange'
    , 4: 'Yellow', 7: 'Purple', 0: 'Magentan'}

tree = BinaryTree(data)
# tree.insert(6, 'Teal')
tree.update({6: 'Teal'})

def displayKeyvalue(key, value):
    print('Key: ', key, 'Value: ', value)

tree.foreach(displayKeyvalue)

print('Item 3 contains: ', tree.get(3))
print('The maximum item is: ',  tree.max_item())

# 这些都是隐藏方法吗
# 可能update也是一个存在的方法
# max_item get 还有foreach这些方法可能是继承自最顶层的对象的方法
#   所有的对象都有的方法

# 二叉树这个lib是刚刚下载的
