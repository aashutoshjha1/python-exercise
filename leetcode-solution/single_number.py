class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num in count.keys():
                count[num] +=1
            else:
                count[num] = 1

        
        return min(count, key=count.get)




class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_num = 0
        for num in nums:
            single_num ^= num   
                
        return single_num
