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



# ===== Execution Flow =====
# s = "sfjeif"

# right=0 => seen{} 
# → s not in seen → {s} → ans=1

# right=1 => {s}
# → f not in seen → {s,f} → ans=2

# right=2 => {s,f}
# → j not in seen → {s,f,j} → ans=3

# right=3 => {s,f,j}
# → e not in seen → {s,f,j,e} → ans=4

# right=4 => {s,f,j,e}
# → i not in seen → {s,f,j,e,i} → ans=5

# ----------------------------------

# right=5 => {s,f,j,e,i}
# → f in seen ❗

# while 開始

# left=0 → remove 's'
# → seen = {f,j,e,i}, left=1

# left=1 → remove 'f'
# → seen = {j,e,i}, left=2

# while 結束（f 已不在）

----------------------------------

# right=5, left=2 => {j,e,i}
# → f not in seen → add f
# → seen = {j,e,i,f}

# ans = 5
