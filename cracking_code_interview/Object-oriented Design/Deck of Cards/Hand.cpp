#include "Hand.hh"

template<typename T>
int Hand<T>::score() {
  int score {0};
  for (auto card : cards) {
    score += card.value();
  }
  return score;
}

template<typename T>
void Hand<T>::addCard(T card) {
  cards.push_back(card);
}