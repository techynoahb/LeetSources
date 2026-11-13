class Solution {
public:
    int lengthOfLastWord(string s) {
        
        int end = s.length() - 1;

        while (s[end] == ' ') {
             end-- ;
        }
        int start = end;
        while (start >= 0 && s[start] != ' ') {
            start-- ;
        }
        
        return end - start;
    }
};
