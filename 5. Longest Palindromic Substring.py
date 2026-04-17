#建議更新跟條件分開寫
#用 動態規劃（Dynamic Programming, DP）
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        max_len=1
        dp=[[False]*n for _ in range(n)]
        #length = 子字串長度 (length = j - i + 1 )=> 頭:至少從1開始(因為 DP 需要先處理最小子問題（長度1）才能推大問題) ; 尾:最多可以到最後，但range最後一個數不算進去，因此+1)
        #i = 子字串的起點 (n-length+1) => i 的最大值 = n - length，但range最後一個數不算進去，因此+1 (i 是子字串起點，為了讓 j 不超出邊界，i 最多只能到 n-length)
        #j = 子字串的終點 (i + length - 1)=> 從length推導的

        for length in range(1,n+1): #先處理子串列長度
            for i in range(n-length+1):  #設定i為子字串的頭，
                j = i + length - 1

                if length==1:
                    dp[i][j]=True
                    result=s[i]  #初始化(base case)：至少有長度1的回文

                elif length==2 and s[i]==s[j]:
                    dp[i][j]=True
                    result=s[i:j+1]  #更新目前找到的最長回文
                    
                
                elif length>2 and s[i]==s[j] and dp[i+1][j-1] :
                    dp[i][j] = True
                
                if dp[i][j] and length>max_len:
                    
                    max_len=length
                    result=s[i:j+1]
                
        return result
                
