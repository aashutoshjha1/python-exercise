def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for word in strs[1::]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix





#The other way:


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        for i in range(len(strs[0])):
            ch = strs[0][i]
            for word in strs[1:]:
                if i >= len(word) or ch != word[i]:
                    return strs[0][:i]
        
        return strs[0]




