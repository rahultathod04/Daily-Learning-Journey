class Solution {
public:
    int lengthOfLongestSubstring(string s) {
         std::vector<int> char_map(128, -1);
        int left = 0;
        int max_len = 0;
        
        for (int right = 0; right < s.length(); ++right) {
            if (char_map[s[right]] >= left) {
                left = char_map[s[right]] + 1;
            }
            char_map[s[right]] = right;
            max_len = std::max(max_len, right - left + 1);
        }
        
        return max_len;
    }
};