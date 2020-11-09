#include <vector>
#include "Card.hh"

template<typename T>
class Deck {
private:
  std::vector<T> cards;
  int dealIndex {0};
public:
  void setDeckOfCards(std::vector<T>);
  void shuffle();
  int remainingCards();
  std::vector<T> dealHand(int);
  T dealCard();
};
