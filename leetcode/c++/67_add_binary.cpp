#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string addBinary(string a, string b) {
        int n = max(a.size(), b.size());
        int carry {0};
        string res {""};

        for (int i = 0; i < n; i++) {
            char d1 = i < a.size() ? a[a.size() - 1 - i] : '0';
            char d2 = i < b.size() ? b[b.size() - 1 - i] : '0';
            if (d1 != d2) {
                res.append(carry == 0 ? "1" : "0");
                carry = carry == 0 ? 0 : 1;
            } else {
                res.append(carry == 0 ? "0" : "1");
                carry = d1 == '1' ? 1 : 0;
            }
        }
        if (carry == 1) {
            res.append("1");
        }
        reverse(res.begin(), res.end());
        return res;
    }
};