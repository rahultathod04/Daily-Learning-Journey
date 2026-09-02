class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // Count frequencies of each number
        unordered_map<int, int> counts;
        for (int num : nums) {
            counts[num]++;
        }
        
        // Group numbers by their frequency
        // Index represents frequency, value is a list of numbers with that frequency
        vector<vector<int>> buckets(nums.size() + 1);
        for (auto& [num, freq] : counts) {
            buckets[freq].push_back(num);
        }
        
        // Collect top k elements from the highest frequencies down to lowest
        vector<int> result;
        for (int i = buckets.size() - 1; i >= 0; --i) {
            for (int num : buckets[i]) {
                result.push_back(num);
                if (result.size() == k) {
                    return result;
                }
            }
        }
        
        return result;
    }
};
