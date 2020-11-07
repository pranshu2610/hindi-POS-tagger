def word_divider(rawFile):
  wordArray = []
  for x in rawFile: #Line by Line txt read
    # print(x)
    x = x.split(' ')
    x = x[0].replace('_', ' ')
    wordArray.append(x)
  return wordArray

# f = open(".\database\idxadverb.txt", "r")
f = open(".\database\example.txt", "r")
a = word_divider(f)
print(a)