class Solution {
public:

    string encode(vector<string>& strs) {
        string es ="";
        for(string s : strs){
            es+=to_string(s.size());
            es+=',';
        }
        es+="+";
        for(string s:strs){
            es+=s;
        }
        return es;
    }

    vector<string> decode(string s) {
        vector<int> lengths;
        string len = "";
        int index;
        for(int i = 0;i<s.length();i++){
            if(s[i] == ','){
                lengths.push_back(stoi(len));
                len = "";
            }
            else if(s[i] == '+'){
                index = i;
                break;
            }
            else{
                len+=s[i] ;
            }          
        }
        index++;
        vector<string> result;
        for(int l : lengths){
            string word = "";
            for(int i = index;i<index+l;i++){
                word+=s[i];
            }
            result.push_back(word);
            index+=l;
        }
        return result;
    }
};
