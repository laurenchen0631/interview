#include "BlackJackHand.hh"
#include <limits>

std::vector<int> BlackJackHand::possibleScores()
{
  std::vector<int> scores {};
  return scores;
}

int BlackJackHand::score()
{
  auto scores {possibleScores()};
  int maxUnder = std::numeric_limits<int>::min();
  int minOver = std::numeric_limits<int>::max();
  for (auto score : scores) {
    if (score > 21 && score < minOver) {
      minOver = score;
    }
    else if (score <= 21 && score > maxUnder) {
      maxUnder = score;
    }
  }
  return maxUnder == std::numeric_limits<int>::min() ? minOver : maxUnder;
}

bool BlackJackHand::busted()
{
  return score() > 21;
}

bool BlackJackHand::is21()
{
  return score() == 21;
}

bool BlackJackHand::isBlackJack()
{
  return false;
}