#include <vector>

template<typename T>
class Hand {
  std::vector<T> cards;
public:
  virtual int score();
  void addCard(T);
};

