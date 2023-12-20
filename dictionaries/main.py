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
