# 感想
# 以前我一直有个误解，就是记忆方法有两种，一种完整描述历史状态，另外一种是把开始和结束记下来，以及这个时间点的状态变化
# 相当于做了一阶导数，或者说是高通滤波，就好像主视眼看到的是高通滤波过的信息，可以看到事物的边缘，简化了看到的信息
# 然后另一只眼睛看到的是面是色彩是低通部分
# 事实上，现在我觉得不是这样的，如果是全量信息，信息量是非常大的。我们在看到事物的时候，自然而然的就对信息进行压缩了。
# 并不存在我以前觉得的两种记忆方法，其实就是压缩前和压缩后，读取压缩过的信息多了解压的部分

# 不代表以前的想法就是错的，只是替换了以前的知识结构，硬盘其实也是又一个选项，就是选择压缩还是不压缩

def lzw_compress(text):
    dictionary = {chr(k): k for k in range(256)}
    print(dictionary)
    encoded = list()
    s = text[0]
    for c in text[1:]:
        # 如果两个字符连接不在ascii码中，则增加到这个字典中，然后把原来的字符放到encoded中
        # 更换成新的字符，跟换的新的字符
        # 如果这个更换的字符已经存在于这个字典中了，那么就再次拼接出新的字典字符，但是这个拼接一定是按照顺序的
        if s + c in dictionary:
            s = s + c
            # 一直拼接到字典中不存在这个字符了，才放到encoded中，就等于是把更多的字符变成小的字符
        else:
            print('> %s' % s)
            encoded.append(dictionary[s])
            print('found: %s compressed as %s' %
                  (s, dictionary[s]))
            dictionary[s + c] = max(dictionary.values()) + 1
            print('New sequence %s indexed as %s' %
                  (s + c, dictionary[s + c]))
            s = c
            print(dictionary)
    encoded.append(dictionary[s])
    print('found: %s compressed as %s'
          % (s, dictionary[s]))
    return encoded

text = 'ABABCABCABC'
compressed = lzw_compress(text)

print('\nCompressed: %s \n' % compressed)

def lzw_decompress(encoded):
    reverse_dictionary = {k:chr(k) for k in range(256)}
    current = encoded[0]
    output = reverse_dictionary[current]
    print('Decompressed %s ' % output)
    print ('> %s' % output)
    # 还是从头开始，第一个应该就是字典，一般来说第一个一定是在字典里
    # 如果是在字典里，那么就开始看第二个，把第二个和第一个拼接起来，然后看，基本上就不再字典里
    for element in encoded[1:]:
        previous = current
        current = element
        if current in reverse_dictionary:
            s = reverse_dictionary[current]
            print('Decompressed %s ' % s)
            output += s
            print('> %s' % output)
            new_index = max(reverse_dictionary.keys()) + 1
            reverse_dictionary[new_index] = reverse_dictionary[previous] + s[0]
            print('New dictinoary entry %s at index %s' %
                  (reverse_dictionary[previous] + s[0], new_index))
            # 如果不再字典里，就按照最大的值，来还原字典，然后把这个字符铁道output中
            # 然后字符s变成上一个字符加上上一个自古的首字符 TODO 理解一下
        else:
            print('Not found:', current, 'Output:', reverse_dictionary[previous]
                  + reverse_dictionary[previous][0])
            s = reverse_dictionary[previous] + reverse_dictionary[previous][0]
            print('New dictionary entry %s at index %s' %
                  (s, max(reverse_dictionary.keys()) + 1))
            reverse_dictionary[max(reverse_dictionary.keys()) + 1] = s
            print('Decompressed %s' % s)
            output += s
            print('> %s' % output)
            # output反正是一直在增加，主要变化的是s
            # 然后如果在字典里，就增加output，然后s就变成了现在这个新的字符
            # 基本上的情况就是不在字典里，然后为什么还可以拼接output呢

            # 看了一下过程就是，如果在字典里，拼接的只是新的字符，然后就直接创造新的字典内容了
            # 那下一个一定还是在字典里，然后又创造了新的字典内容
            # 通过s[0]来还原AB
            # 如果找不到，那就是还没有还原出来的字典，这个字典还不够，也就是previous其实就是上一个字符，上一个字符一定是在字典离了
            # 举个例子，上一个字符就是ABAB了，然后他在字典中是257，现在把257拼接上

            # 乱了，再来一遍
            # 如果在字典里面，就直接拼接，然后换成新的s是BA，存到字典里面
            # 然后发现256是AB，在字典里面，然后s就变成了BA
            # 然后256，发现在字典里，就拼接上AB，生成新的字典BA
            # 然后C在字典里，就生成新的字典ABC，存到字典里

            # 还是看不懂，就没有not found，全部都是found
            # 全部都是found！！
            # 显示found，然后拼出新的字典了，然后还是founcAB，就评出新的字典ABAB
            # 然后c还是found就拼出ABC，这时候previous是C
            # 然后还是foundABC，就把C和ABC的首字母A平成CA
            # 然后还是foundABC，就把ABC和ABC的首字母拼成ABCA

            # 也就是说把可能的字符都提前压缩好了。顺序基本上就是按照一定的套路就安排好了
            # 那什么时候会找不到呢

            # 台风来了，看这个看到两点钟，躺下了还在想，心脏不舒服
            # python工程师的工资一点都不高，golang工程师的工资也不怎么高。怎么样在能变成资深，或者架构师
    return output

print('\ndecompressed string : %s' % lzw_decompress(compressed))
print('original string was : %s' % text)

print('\ndecompressed string : %s' % lzw_decompress(lzw_compress(
    "onpo3qinvn3[0[nfejd[23[j3d[2n3fo32132132132132121313"
)))
print('\ndecompressed string : %s' % lzw_decompress(lzw_compress(
    "onpo3qinvn3[0[nfejd[23[j3d[2n3fo432 432 432 432 432 432 432 432 432 432 432 432 4444321313"
)))

# 想要找不到，必须又相同的重复字符串重复3次以上，这样的话，就把需要用已经存在的字符不断的在凭借上去
# 预想在压缩的时候，会不断的出现已经存在的单个的字符串压缩到压缩后文件中
# 不存在的一定就是以前的字符串的第一个和现在新的字符串进行拼接
# 因为重复字符串如果是3个字符的，在一开始就会是已经存在，然后慢慢拼接到完全重复的时候，才会说是不存在了

# 其实还是一知半解，但是结果是正确的
# 测试结果是如果是3个字符的需要3*2*1次重复才能进入第二个循环
# 4个的话是12次