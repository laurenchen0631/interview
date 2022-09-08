#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int calculate(string s) {
        vector<int> numStack;
        vector<char> opStack;
        int i = 0;
        while (i < s.size()) {
            if (s[i++] == ' ') {
                i++;
                continue;
            }
            if (s[i] == '+' || s[i] == '-' || s[i] == '*' || s[i] == '/') {
                opStack.push_back(s[i]);
                i++;
                continue;
            }
            int num = 0;
            while (i < s.size() && s[i] >= '0' && s[i] <= '9') {
                num = num * 10 + s[i] - '0';
                i++;
            }
            numStack.push_back(num);
            if (opStack.size() > 0 && (opStack.back() == '*' || opStack.back() == '/')) {
                int num2 = numStack.back();
                numStack.pop_back();
                int num1 = numStack.back();
                numStack.pop_back();
                char op = opStack.back();
                opStack.pop_back();
                if (op == '*') {
                    numStack.push_back(num1 * num2);
                } else {
                    numStack.push_back(num1 / num2);
                }
            }
        }

        while (opStack.size() > 0) {
            int num2 = numStack.back();
            numStack.pop_back();
            int num1 = numStack.back();
            numStack.pop_back();
            char op = opStack.back();
            opStack.pop_back();
            if (op == '+') {
                numStack.push_back(num1 + num2);
            } else {
                numStack.push_back(num1 - num2);
            }
        }
        return numStack.back();

    }
};