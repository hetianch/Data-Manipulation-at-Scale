import MapReduce
import sys

"""
asymetric friend count by MapReduce
Note: you can only access one entry with same key at a time in reducer.
## choosing the "key" of mapper is the most important step!!
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    perA = record[0]
    perB = record[1]
    val = perA + ' ' + perB
    record.sort()
    key = ''.join(record)
    mr.emit_intermediate(key, val)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    pair = len(list_of_values)
    if pair <2: #miss friend,person pair

        friend = list_of_values[0].split()[0]
        person = list_of_values[0].split()[1]
        mr.emit((friend,person))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
