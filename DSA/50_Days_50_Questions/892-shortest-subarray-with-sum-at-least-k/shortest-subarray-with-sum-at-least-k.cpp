class Solution {
public:
    int shortestSubarray(vector<int>& nums, int k) {
       int n = nums.size();
        std::vector<long long> P(n + 1, 0);
        
        // Compute prefix sums
        for (int i = 0; i < n; ++i) {
            P[i + 1] = P[i] + nums[i];
        }
        
        int min_len = n + 1;
        std::deque<int> dq; // Stores indices
        
        for (int j = 0; j <= n; ++j) {
            // Check if window sum is valid
            while (!dq.empty() && P[j] - P[dq.front()] >= k) {
                min_len = std::min(min_len, j - dq.front());
                dq.pop_front();
            }
            
            // Maintain monotonic increasing order
            while (!dq.empty() && P[j] <= P[dq.back()]) {
                dq.pop_back();
            }
            
            dq.push_back(j);
        }
        
        return min_len <= n ? min_len : -1;  
    }
};