def new_binary_search(data, target, low, high):
    
   if data:
       if len(data) == 1:
            if data[0] == target:
                print("data found as only one element in sequence")
            else:
                print("taget not found")
   if low > high:
       print("data not found")
       return False
   else:
      
       mid = (high+low)//2
       if target == data[mid]:
            print("target number {0} found on in sequence on index {1}".format(target,data.index(target)))
       else:
           if target < data[mid]:
                new_binary_search(data,target, low, mid-1)
           else:
                new_binary_search(data,target, mid+1, high)
       

data = [2,4,6,7,8,10,16,18,20,24,25]
low = 0
high = len(data) 
target = 10
new_binary_search(data, target,low, high)

