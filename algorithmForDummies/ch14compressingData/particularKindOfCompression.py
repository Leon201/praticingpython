import urllib.request
import zlib

from random import randint

url = "http://gutenberg.pglaf.org/1/6/6/1661/1661.txt"
sh = urllib.request.urlopen(url).read().decode('utf-8')
sh_length = len(sh)
rnd = ''.join([chr(randint(0, 126)) for k in range(sh_length)])


# 这里的字符串的语法直接使用了join
# []应该是个数组
# 数组中是0到126的字符
# 直接在这个字符的后面使用了for，然后for的元素是长度内的1到原来文件的长度
# # 意思就是如果放在了for的前面，那就不是一个函数了，直接就是return的元素

# 用ascii来编码，然后在压缩这样的文件
def zipped(text):
    return len(zlib.compress(text.encode("ascii")))


print("Original size for both texts: %s characters" %
      sh_length)

print("The Adventures of Sherlock holmes to %s" %
      zipped(sh))

# 随机的字符串压缩下来字符反而更多了，还不如不压缩
print("Random file to %s " % zipped(rnd))
