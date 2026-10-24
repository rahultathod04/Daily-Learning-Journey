class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int n = nums.size();
        int sum  = 0;
        int ans = INT_MAX;
        int left = 0;

        for(int r=0; r<n; r++){
            sum += nums[r];

            while (sum>=target){
                int win_len = r - left + 1;
                ans = min(ans , win_len);

                sum -= nums[left];
                left ++;
            }
        }
         return (ans == INT_MAX) ? 0 : ans; 

        
    }
};