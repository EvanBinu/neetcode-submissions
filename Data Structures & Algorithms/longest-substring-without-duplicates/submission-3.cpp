class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> smap;
        int l = 0;
        int mlen= 0;
        for(int r = 0;r<s.size();r++){
            while(smap.count(s[r])){
                smap.erase(s[l]);
                l++;
            }
            smap.insert(s[r]);
            mlen = max(mlen,r - l + 1);
        }
        return mlen;
    }
};
