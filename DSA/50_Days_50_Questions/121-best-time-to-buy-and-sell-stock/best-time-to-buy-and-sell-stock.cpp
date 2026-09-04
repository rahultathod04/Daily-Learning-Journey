class Solution {
public:
    int maxProfit(vector<int>& prices) {
       int n = prices.size();
       int max_prf = 0;
       int buy = prices[0];

       for(int i=1; i<n; i++){
        int current_prf = prices[i] - buy;

        if(current_prf > max_prf){
            max_prf = current_prf;
        }
        if(prices[i]<buy){
            buy = prices[i];
        }
       }
       return max_prf;
    }
};