class Solution {
private:
    // Helper function to check if a specific slice of the string is a palindrome
    bool isPaliSlice(const string& s, int l, int r) {
        while (l < r) {
            if (s[l] != s[r]) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }

public:
    bool validPalindrome(string s) {
        int left = 0;
        int right = s.length() - 1;
        
        while (left < right) {
            if (s[left] != s[right]) {
                // Fork in the road: skip s[left] OR skip s[right]
                return isPaliSlice(s, left + 1, right) || isPaliSlice(s, left, right - 1);
            }
            left++;
            right--;
        }
        
        return true;
    }
};
