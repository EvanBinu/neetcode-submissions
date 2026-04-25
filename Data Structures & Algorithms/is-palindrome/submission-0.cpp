class Solution {
public:
    bool isPalindrome(string s) {
        string ns ="";
        for(char ch : s){
            if(isalnum(ch)){
                ns+=tolower(ch);
            }
        }
        int n = ns.length();
        for(int i = 0;i<n/2;i++){
            if(ns[i] != ns[n-i-1]) return false;
        }
        return true;
    }
};
