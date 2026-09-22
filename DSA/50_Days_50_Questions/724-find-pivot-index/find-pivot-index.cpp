class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int n = nums.size();
        int total_sum = 0;
        for(int i=0; i<n; i++){
            total_sum +=nums[i];
        }

        int left = 0;
        for(int i=0; i<n; i++){
            int right = total_sum - left - nums[i];
            
            if(left == right){
                return i;
            }
            left += nums[i];
        }
        return -1;
    }
};