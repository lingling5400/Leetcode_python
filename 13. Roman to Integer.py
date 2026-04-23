class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result=0
        i=0
        while i<len(s):
            current=self.StrToNum(s[i])
            next=0
            if i + 1 < len(s):
                next=self.StrToNum(s[i+1])


            if next >current:
                result+=next-current
                i+=2
            else:
                result+=current
                i+=1
        return result

   
    def StrToNum(self, s): #def記得縮排
        return {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }.get(s, 0)
#get(s,0), Python 字典（dict）常用方法
#語法:my_dict.get(key, default_value)
#預設為0代表: 如果 s 不在字典裡就回傳0
