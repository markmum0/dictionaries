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
    print(wds)
    for w in wds:
        # adding the words in the list into the dictionary both new and existing
        if w in di:
            # if the word exist the value is added
            di[w] = di[w]+1
        else:
            # if the word is new is assigned the value 1
            di[w] = 1
print(di)