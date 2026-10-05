class Solution {
public:
    int maxAbsoluteSum(vector<int>& nums) {
        int n = nums.size();
        int max_sum =nums[0];
        int min_sum = nums[0];
        int sum1=nums[0];
        int sum2 = nums[0];

        for(int i=1; i<n; i++){
            sum1 = max(sum1+nums[i], nums[i]);
            max_sum = max(sum1, max_sum);

            sum2 = min(sum2+nums[i], nums[i]);
            min_sum = min(min_sum, sum2);
        }

        return max(abs(max_sum), abs(min_sum));
    }
};