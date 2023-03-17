#include <string>
#include <unordered_map>

using namespace std;

class Trie {
public:
    Trie() {

    }
    
    void insert(string word) {
        Trie* node = this;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = make_unique<Trie>();
            }
            node = node->children[c].get();
        }
        node->isEnd = true;
    }
    
    bool search(string word) {
        Trie* node = this;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                return false;
            }
            node = node->children[c].get();
        }
        return node->isEnd;
    }
    
    bool startsWith(string prefix) {
        Trie* node = this;
        for (char c : prefix) {
            if (node->children.find(c) == node->children.end()) {
                return false;
            }
            node = node->children[c].get();
        }
        return true;
    }
private:
    unordered_map<char, unique_ptr<Trie>> children;
    bool isEnd {false};
};
