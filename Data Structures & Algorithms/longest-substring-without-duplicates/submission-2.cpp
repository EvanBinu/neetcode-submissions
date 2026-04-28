class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char,int> count;
        int mlen = 0;
        int l = 0;
        for(int r = 0;r<s.size();r++){
            if(count.find(s[r]) != count.end()){
                l = max(count[s[r]]+1,l);
            }
                count[s[r]] = r;
                mlen = max(mlen,r- l+1);
            
        }
        return mlen;
        
    }
};
