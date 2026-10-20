class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int r = matrix.size();
        int c = matrix[0].size();

        int s = 0;
        int end = r*c-1;

        while(s<=end){
            int mid = s +(end-s)/2;
            int mid_val = matrix[mid/c][mid%c];
            if(mid_val==target){
                return true;
            }else if(mid_val<target){
                s = mid +1;
            }else{
                end = mid-1;
            }
        }return false;
    }
};