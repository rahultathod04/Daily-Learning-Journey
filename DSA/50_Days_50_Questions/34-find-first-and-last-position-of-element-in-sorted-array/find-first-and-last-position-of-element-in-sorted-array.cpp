class Solution {
public:
    int Left(vector<int>& nums, int target, int n){
        int left_most = -1;
        int l = 0;
        int r = n-1;

        while(l<=r){
            int mid = l+(r-l)/2;
            if(nums[mid]==target){
                left_most = mid;
                r = mid-1;
            }else if(nums[mid]<target){
                l=mid+1;
            }else{
                r=mid-1;
            }

        }return left_most;
    }

    int Right(vector<int>& nums, int target, int n){
        int right_most = -1;
        int l = 0;
        int r = n-1;

        while(l<=r){
            int mid = l+(r-l)/2;
            if(nums[mid]==target){
                right_most = mid;
                l = mid+1;
            }else if(nums[mid]<target){
                l=mid+1;
            }else{
                r=mid-1;
            }

        }return right_most;
    }
    vector<int> searchRange(vector<int>& nums, int target) {
        int n = nums.size();
        int left = Left(nums, target, n);
        int right = Right(nums, target, n);
        return {left, right};
    }
};