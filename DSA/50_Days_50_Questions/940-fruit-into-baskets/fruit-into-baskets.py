class Solution(object):
    def totalFruit(self, fruits):
        n = len(fruits)
        count = {}
        ans = 0
        l = 0

        for r in range(n):
            f = fruits[r]
            if f in count:
                count[f] +=1
            else:
                count[f] = 1
            
            while(len(count)>2):
                count[fruits[l]]-=1

                if count[fruits[l]] == 0:
                    del count[fruits[l]]

                l+=1

            ans = max(ans , r-l+1)

        return ans
        