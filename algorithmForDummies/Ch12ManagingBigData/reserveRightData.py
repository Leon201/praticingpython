import string
datastream = list(string.ascii_uppercase) + list(string.ascii_lowercase)

print(datastream)
print(string.ascii_uppercase)

from random import seed, randint
seed(9) # seed不变的话，结果是会保持不变的
sample_size = 5
sample = []

for index, element in enumerate(datastream):
    if index < sample_size:
        sample.append(element)
    else:
        drawn = randint(0, index)

        if drawn < sample_size:
            sample[drawn] = element
print (sample)