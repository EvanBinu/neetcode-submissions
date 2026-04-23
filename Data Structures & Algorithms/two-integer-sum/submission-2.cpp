class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> map;
        for(int i = 0;i<nums.size();i++){
            map[nums[i]] = i;
        }
        vector<int> index;
        for(int i=0;i<nums.size();i++){
            int value = target - nums[i];
            if(map.count(value) && map[value]!=i){
                index.push_back(i);
                index.push_back(map[value]);
                break;
            }
        }
        return index;
    }
};
