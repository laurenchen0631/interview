#include <string>
#include <stack>

using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        string res = "";
        stack<char> st;
        for (auto c : s) {
            if (c != ' ') {
                st.push(c);
                continue;
            }

            while (!st.empty()) {
                res += st.top();
                st.pop();
            }
            res += c;
        }
        while (!st.empty()) {
            res += st.top();
            st.pop();
        }
        return res;
    }
};