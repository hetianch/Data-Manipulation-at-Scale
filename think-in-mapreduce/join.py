import MapReduce
import sys

"""
Join implemented by MapReduce
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: order
    # value: other files
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: word
    # value: document identifier
    l = []
    for v in list_of_values:
      if v[0] == "order":
        l.extend(v)
      else:
        x = list(l)   # cannot l.extend that will make the list longer and longer
        x.extend(v)
        mr.emit(x)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
