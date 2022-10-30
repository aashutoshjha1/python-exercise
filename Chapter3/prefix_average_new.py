def prefix_average1(S):
      n = len(S)
      A=[0]*n
      for j in range(n):
          total = sum(S[0:j+1])
          avg = total/(j+1)
          A[j] = avg

      return A

list1 = [2,4,5,6,7,8]
print(prefix_average1(list1))
    

