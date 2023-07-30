def rec_sum(n):
   
    """ Get sequnce of no as input and return sum of no. as output"""
    print(n)
    if len(n) == 0:
         return False
    else:
       #print( n[0] + rec_sum(n[1:(len(n)-1)]))
       total =  n[0] + rec_sum(n[1:])
       return total
          


list1 = [2,3,4,5,6]
print(rec_sum(list1))

          
          
