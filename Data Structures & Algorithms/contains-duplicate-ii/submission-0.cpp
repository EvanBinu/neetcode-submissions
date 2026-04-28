class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_set<int> smap;
        int l = 0;
        for(int r = 0;r<nums.size();r++){
            while(smap.count(nums[r])){
                if(abs(r-l) <= k) return true;
                else{
                    smap.erase(nums[l]);
                    l++;
                }
            }
            smap.insert(nums[r]);
            
        }
        return false;
    }
};