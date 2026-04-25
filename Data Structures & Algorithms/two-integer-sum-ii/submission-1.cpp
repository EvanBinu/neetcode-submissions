class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0;
        int right = numbers.size() - 1;
        vector<int> result;
        while(left<right){
            int csum = numbers[left]+numbers[right];
            if( csum== target){
                result.push_back(left+1);
                result.push_back(right+1);
                break;
            }
            if(csum>=target) right--;
            else if(csum<target) left++;
        }
        return result;
    }
};
