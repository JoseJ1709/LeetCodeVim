class Solution(object):
    def longestCommonPrefix(self,strs):
        word = strs[0]
        a = []
        for i in range(len(word)):
            c = word[i]
            for j in strs[1:]:
                if i>= len(j) or c != j[i]:
                    return ''.join(a) 
            a.append(c)
        
        return ''.join(a)