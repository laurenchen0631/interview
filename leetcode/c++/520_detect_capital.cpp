#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool detectCapitalUse(string word) {
        auto n {word.size()};
        if (n==1) return true;

        int cnt {0};
        for (auto c: word) {
            if (isupper(c)) cnt++;
        }
        if (cnt==0 || cnt==n) return true;
        if (cnt==1 && isupper(word[0])) return true;
        return false;
    }
};