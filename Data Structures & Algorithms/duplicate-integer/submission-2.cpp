class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int,int> map;
        for(int x : nums){
            map[x]++;
        }
        for(const auto& [num,count] : map){
            if(count > 1) return true;

        }
        return false;
    }
};