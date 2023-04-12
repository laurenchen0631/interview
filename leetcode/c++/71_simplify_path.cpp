#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string simplifyPath(string path) {
        vector<string> stack;
        int i = 0;
        while (i < path.size()) {
            while (i < path.size() && path[i] == '/') {
                i++;
            }
            if (i == path.size()) {
                break;
            }
            int start = i;
            while (i < path.size() && path[i] != '/') {
                i++;
            }
            int end = i - 1;
            string sub = path.substr(start, end - start + 1);
            if (sub == "..") {
                if (!stack.empty()) {
                    stack.pop_back();
                }
            } else if (sub != ".") {
                stack.push_back(sub);
            }
        }
        if (stack.empty()) {
            return "/";
        }
        string res;
        for (auto s : stack) {
            res += "/" + s;
        }
        return res;
    }
};