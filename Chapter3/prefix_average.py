def prefix_average1(S):
      n = len(S)
      A=[0]*n
      for j in range(n):
          total = 0
          for i in range(j + 1):
               total += S[i]
               A[j] = total / (j+1)
       
      return A

list1 = [2,4,5,6,7,8]
print(prefix_average1(list1))
    

