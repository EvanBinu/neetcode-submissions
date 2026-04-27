class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        int l =0;
        int r =0;
        int  p =0;
        for(int i = 0;i<prices.size();i++){
            if(prices[l] > prices[i]){
                l = i;
                r = i;
            }
            else if(prices[r] < prices[i]){
                r = i;
                p = prices[r] - prices[l];
                profit = max(p,profit); 
            }
            
        }
        return profit;
    }
};
