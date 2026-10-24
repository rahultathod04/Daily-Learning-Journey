class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""
            
        start, end = 0, 0
        
        def expand_around_center(left, right):
            # Expand outwards as long as characters match and boundaries are valid
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the length of the palindrome found
            return right - left - 1

        for i in range(len(s)):
            # Case 1: Odd length palindromes (e.g., "aba", center is 'b')
            len1 = expand_around_center(i, i)
            
            # Case 2: Even length palindromes (e.g., "abba", center is between 'b' and 'b')
            len2 = expand_around_center(i, i + 1)
            
            # Find the maximum length between both cases
            max_len = max(len1, len2)
            
            # If we found a longer palindrome, update our starting and ending boundaries
            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        return s[start : end + 1]
