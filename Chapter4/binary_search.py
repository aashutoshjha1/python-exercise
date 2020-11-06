def binary_search(data_seq, num):
    """ This function will get a sorted array/sequence 
        and perform binary search to get required data.
    """
    mid = 0
    low = 0
    if (len(data_seq)-1) > 0:
         mid = (len(data_seq)-1)//2
         print(mid)
    if  data_seq[mid] == num:
       print("no. {} found in list {}".format(num, data_seq[mid]))
    elif data_seq[mid] > num:
        low = 0
        return binary_search(data_seq[0:(mid-1)], num)
    else:
        print(data_seq[(mid+1):-1])
        low = mid+1
        return binary_search(data_seq[(low)::], num)
        
list1 = [1,2,3,4,5,6,7,8]
mid = (len(list1)-1)//2
print(list1[mid])
binary_search(list1, 3)

    
