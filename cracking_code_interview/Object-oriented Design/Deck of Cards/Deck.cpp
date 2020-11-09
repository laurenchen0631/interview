#include "Deck.hh"
#include <random>
#include <algorithm>
#include <chrono> // std::chrono::system_clock

template<typename T>
void Deck<T>::setDeckOfCards(std::vector<T> deckOfCards)
{
  cards = deckOfCards;
}

template<typename T>
void Deck<T>::shuffle()
{
  unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
  std::shuffle(card.begin(), card.end(), std::default_random_engine(seed));
}

template<typename T>
int Deck<T>::remainingCards()
{
  return cards.size() - dealIndex;
}

template<typename T>
std::vector<T> Deck<T>::dealHand(int number)
{
  std::vector<T> hand {} 
  if (remainingCards() < number) {
    return hand;
  }

  while (hand.size() < number) {
    hand.push_back(dealCard());
  }
  return hand;
}

template<typename T>
T Deck<T>::dealCard() {
  auto card = cards.at(dealIndex++);
  return card
}

