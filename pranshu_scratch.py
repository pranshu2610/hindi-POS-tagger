def word_divider(rawFile):
  wordArray = []
  for x in rawFile: #Line by Line txt read
    # print(x)
    x = x.split(' ')
    x = x[0].replace('_', ' ')
    wordArray.append(x)
  return wordArray

# f = open(".\database\idxadverb.txt", "r")
f = open(".\database\idxverb.txt", "r")
a = word_divider(f)
a = a[:1]
print(b)
# raw_string = r"{}".format(a)

