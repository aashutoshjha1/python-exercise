def minmax(data):
    """
       This function takes a sequence of list and return
       tumple with min and max no. without using inbuild min max
       function.
    """
    min = None
    max = None
    for i in data:
       if not min in data:
           min = i
       if i < min:
          min = i
       if i > max:
           max = i
    return(min, max)

data = [3,4,5,6,20,1,25]
print(minmax(data))
