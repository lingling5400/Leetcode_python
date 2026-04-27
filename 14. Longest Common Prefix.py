class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""

        result=""
        for i in range(len(strs[0])):
            for word in strs:
                if i >= len(word) or word[i] != strs[0][i]:
                    return result
            result+=strs[0][i]

        return result  
#-----------------------------------------------------------------------------------------------
#for 每一個位置 i:
#     for 每一個字串 word:
#            比 word[i]
