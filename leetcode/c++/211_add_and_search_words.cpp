#include <string>
#include <unordered_map>
#include <memory>

using namespace std;

struct TrieNode {
    unordered_map<char, unique_ptr<TrieNode>> children;
    bool isEnd {false};
};

class WordDictionary {
public:
    WordDictionary() {
        
    }
    
    void addWord(string word) {
        TrieNode* node = root.get();
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = make_unique<TrieNode>();
            }
            node = node->children[c].get();
        }
        node->isEnd = true;
    }
    
    bool search(string word) {
        return searchImpl(0, root.get(), word);
    }
private:
    unique_ptr<TrieNode> root {make_unique<TrieNode>()};

    bool searchImpl(int i, TrieNode* node, string& word) {
        if (i == word.size())
            return node->isEnd;
        if (word[i] == '.') {
            for (auto& [c, child] : node->children) {
                if (searchImpl(i + 1, child.get(), word))
                    return true;
            }
            return false;
        } else {
            if (node->children.find(word[i]) == node->children.end()) {
                return false;
            }
            return searchImpl(i + 1, node->children[word[i]].get(), word);
        }
    }

};
