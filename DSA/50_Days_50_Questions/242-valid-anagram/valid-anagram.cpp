class Solution {
public:
    bool isAnagram(string s, string t) {
         if (s.length() != t.length()) {
        return false;
    }
    
    // Fixed-size frequency array for 'a' through 'z'
    int count[26] = {0};
    
    // Increment for s, decrement for t
    for (size_t i = 0; i < s.length(); ++i) {
        count[s[i] - 'a']++;
        count[t[i] - 'a']--;
    }
    
    // If any element is non-zero, they are not anagrams
    for (int i = 0; i < 26; ++i) {
        if (count[i] != 0) {
            return false;
        }
    }
    
    return true;
    }
};