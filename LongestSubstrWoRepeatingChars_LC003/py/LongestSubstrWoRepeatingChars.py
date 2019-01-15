class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        
        i, j starts from 0
        if s[i] is not in hashmap, put its index in
        if s[i] is already in hashmap, find the previous s[i]'s index
        find the max of previous s[i]'s index and j
        
        e.g. abcafcbdx
        when it goes to the 2nd c, the non-repeating substring is after the first c (j=3) to 2nd c, i.e. afc
        then the next element is the 2nd b
        previous b is at index 1 (s[b]+1 = 2), we can't use cafcb (from index 2 to 6) because it has repeating c inside 
        we shall use max(j=3, s[b]+1), which is 3

        count the length of the substring by max(i-j+1, res)
        """
        strDict = {}
        j = 0
        res = 0
        for i in range(len(s)):
            if s[i] in strDict:
                j = max(j, strDict[s[i]]+1)
            strDict[s[i]] = i
            res = max(i-j+1, res)

        return res

s = Solution()
str1 = "abcafcbdx"
ret = s.lengthOfLongestSubstring(str1)
print(ret)
