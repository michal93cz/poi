from ast import literal_eval as createTuple
from pprint import pprint

tupleList = []

with open("tuples.txt","r") as infile:
  for line in infile:
    tupleList.append(createTuple(line))

resultList = []
f = open("./results_without_repeats/detroit_manhattan_200m.txt", "w+")
for key, value in tupleList:
  if key[0] != key[1]:
    f.write('(' + str(key[0]) + ', ' + str(key[1]) + ') ' + str(value) + '\n')
    resultList.append(((key[0], key[1]), value))

f.close()
pprint(resultList)
