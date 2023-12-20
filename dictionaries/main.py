# entering and opening the files
# only 2 files in the dir intro.txt and clown.txt
name = input('Enter file name: ')
if len(name) < 1:
    var = name = 'clown.txt'
handle = open(name)
# empty dictionary
di = dict()
# cleaning up the values and putting them into a list
for line in handle:
    words = line.rstrip()
    wds = words.split()
    # print(wds)
    for w in wds:
        # this idiom simplifies the process of adding keys and values in the dictionary.
        di[w] = di.get(w, 0) + 1

print(di)

# This creates a list of tuples that can be sorted.
# y = sorted(di.items())
# print(y)

# this sorts the tuples as per the values so that one can identify the most used word
temp = list()
for k, v in di.items():
    newtup = (v, k)
    temp.append(newtup)
    # the , reverse=True sorts from most used words to the least used
temp = (sorted(temp, reverse=True))

# if I want to know 5 of the most used words
for v, k in temp[:5]:
    print(k,v)
