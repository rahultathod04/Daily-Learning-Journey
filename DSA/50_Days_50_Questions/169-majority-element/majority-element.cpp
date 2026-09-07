class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n = nums.size();
        int ans = nums[0];
        int frq = 0;

        for(int i=0; i<n; i++){
            if(frq == 0){
                ans = nums[i];
            }
            if(ans == nums[i]){
                frq++;
            }else{
                frq--;
            }
        }
        return ans ;
    }
};