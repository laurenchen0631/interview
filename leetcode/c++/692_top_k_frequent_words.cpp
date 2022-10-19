#include <vector>
#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <queue>

using namespace std;

class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> count;
        for (auto& word : words) count[word]++;

        vector<pair<int, string>> heap;
        for (auto& [word, freq] : count) heap.push_back(make_pair(-freq, word));
        make_heap(heap.begin(), heap.end(), greater<pair<int, string>>()); // min heap

        vector<string> res;
        for (int i = 0; i < k; i++) {
            pop_heap(heap.begin(), heap.end(), greater<pair<int, string>>());
            res.push_back(heap.back().second);
            heap.pop_back();
        }
        return res;
    }

    vector<string> topKFrequentPQ(vector<string>& words, int k) {
        unordered_map<string, int> cnt;
        vector<pair<int, string>> candidates;
        vector<string> res;
        priority_queue<pair<int, string>> h;
        for (string& word : words) cnt[word]++;
        for (auto& p : cnt) {
            h.push({-p.second, p.first});
            if (h.size() > k) h.pop();
        }
        while (!h.empty()) {
            candidates.push_back(h.top());
            h.pop();
        }
        sort(candidates.begin(), candidates.end());
        for (auto& p : candidates) res.push_back(p.second);
        return res;
    }
};