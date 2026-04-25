class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.empty()) return 0;
        if(nums.size()==1)return 1;
        sort(nums.begin(),nums.end());
        unordered_set<int> numss;
        for(int x : nums){
            numss.insert(x);
        }
        vector<int> nnums;
        for( const auto& n : numss){
            nnums.push_back(n);
        }
        sort(nnums.begin(),nnums.end());
        int left = 0;
        int right = 1;
        int mcount = 1;
        int count = 1;
        for(int i = 0;i<nnums.size();i++){
            if((nnums[left] + 1) == nnums[right]) {
                count++;
                mcount = max(mcount,count);
                left++;right++;
            }
            else{
                count = 1;
                left++;
                right++;
            }            
        }
        return mcount;
    }
};
