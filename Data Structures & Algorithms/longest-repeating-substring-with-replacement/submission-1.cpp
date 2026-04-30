class Solution {
public:
    int characterReplacement(string s, int k) {
        vector<int> counts(26,0);
        int l = 0;
        int maxcount = 0;
        int maxlen = 0;
        int n = s.size();
        for(int i = 0;i<n;i++){
            counts[s[i]-'A']++;
            maxcount = max(maxcount,counts[s[i]-'A']);
            while((i-l+1) - maxcount > k){
                counts[s[l]-'A']--;
                l++;
            }
            maxlen=max(maxlen,i-l+1);
        }
        return maxlen;
    }
};
