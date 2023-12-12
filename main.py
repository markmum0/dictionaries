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
        # adding the words in the list into the dictionary both new and existing by using the .get function
        di[w] = di.get(w, 0) + 1
print(di)

# the most used word and by how much
largest_number = -1
most_word = None
for k, v in di.items():
    if v > largest_number:
        largest_number = v
        most_word = k
print(most_word, largest_number)
