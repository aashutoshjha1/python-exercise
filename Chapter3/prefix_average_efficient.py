def prefix_average1(S):
      n = len(S)
      A=[0]*n
      total = 0
      for i in range(n):
          total +=S[i]
          avg = total/(i+1)
          A[i] = avg

      return A

list1 = [2,4,5,6,7,8]
print(prefix_average1(list1))
    

