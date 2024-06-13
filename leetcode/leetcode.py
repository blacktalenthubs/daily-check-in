class Solution:


    def is_anagram(self,s,t):
        if len(s) != len(t):
            return False

        dic = {}

        for char in s:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] +=1

        for char2 in t:
            if char2 in dic:
                dic[char2] -=1
            else:
                return False

        for val in dic.values():
            if val !=0:
                return False

        return True

test = Solution()
print(test.is_anagram("jar","jam"))