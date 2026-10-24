class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        int n = nums.size();

        if(k<=1){
            return 0;
        }
        int l =0, ans=0, prd=1;

        for(int r=0; r<n; r++){
            prd*=nums[r];

            while(prd>=k){
                prd/=nums[l];
                l++;
            }

            ans += (r-l)+1;
        }
        return ans;
    }
};