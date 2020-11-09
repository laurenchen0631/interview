#include "Hand.hh"
#include "BlackJackCard.hh"

class BlackJackHand : public Hand<BlackJackCard> {
  std::vector<int> possibleScores();
public:
  int score() override;
  bool busted();
  bool is21();
  bool isBlackJack();
};