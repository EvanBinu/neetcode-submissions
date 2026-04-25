class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numset(nums.begin(),nums.end());
        int lc = 0;
        for(int num : numset){
            if(numset.find(num-1) == numset.end()){
                int currentnum = num;
                int cstreak = 1;
                while(numset.find(currentnum+1)!=numset.end()){
                    currentnum++;
                    cstreak++;
                }
                lc = max(lc,cstreak);
            }
        }
        return lc;
    }
};
