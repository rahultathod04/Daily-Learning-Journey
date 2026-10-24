class Solution(object):
    def findAnagrams(self, s, p):
        k = len(p)
        n = len(s)

        count = [0]*26
        for ch in p:
                count[ord(ch)-ord('a')]+=1
        
        i, j = 0,0
        result = []

        while j<n:

            ind = ord(s[j]) - ord('a')
            count[ind]-=1

            if(j-i+1==k):
                if all(v==0 for v in count):
                    result.append(i)

                count[ord(s[i])- ord('a')]+=1
                i+=1
            j+=1
        return result 