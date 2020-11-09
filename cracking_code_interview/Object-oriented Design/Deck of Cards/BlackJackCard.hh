#include "Card.hh"

/*
  In BlackJack,
    the value of J, Q, K is 10
    the value of A can be 1 or 11
*/
class BlackJackCard : public Card {
private:
  bool isAce();
  bool isFaceCard();
public:
  int value() override;
  int minValue();
  int maxValue();
};