class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> count;
        for(int num : nums){
            count[num]++;
        }
        vector<pair<int,int>> arr;
        for(const auto& [num,occ] : count){
            arr.push_back({occ,num});
        }
        sort(arr.rbegin(),arr.rend());
        vector<int> result;
        for(int i = 0;i<k;i++){
            result.push_back(arr[i].second);
        }
        return result;
    }
};
