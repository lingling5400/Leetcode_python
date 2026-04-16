class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Sliding Window
        seen=set() #子集合
        left=0
        ans=0

        for right in range(len(s)):
            while s[right] in seen:  #重複時
                seen.remove(s[left])
                left+=1
            
            if s[right] not in seen:
                seen.add(s[right])
                ans=max(ans,right-left+1)
        return ans
