class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for word in strs[1:]:
            new_prefix = ''
            for i in range(min(len(prefix), len(word))):
                if word[i] != prefix[i]:
                    break
                
                new_prefix += word[i]
            prefix = new_prefix
        
        return prefix
                    

