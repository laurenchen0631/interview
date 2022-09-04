#include <map>
#include <algorithm>
#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        map<char,int> lastChar {};
        int res {0};
        int l {0};
        for (int i = 0; i < s.length(); ++i) {
            auto c {s[i]};
            if (lastChar.find(c) != lastChar.end()) {
                l = max(l, lastChar[c]);
            }
            res = max(res, i - l + 1);
            lastChar[c] = i;
        }
        return res;
    }
};