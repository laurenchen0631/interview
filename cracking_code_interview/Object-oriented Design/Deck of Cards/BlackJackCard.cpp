#include "BlackJackCard.hh"

bool BlackJackCard::isAce()
{
  return faceValue == 1;
}

bool BlackJackCard::isFaceCard()
{
  return  faceValue >= 11 && faceValue <= 13;
}

int BlackJackCard::value()
{
  if (isAce()) return 1;
  if (isFaceCard()) return 10;
  return faceValue;
}

int BlackJackCard::minValue()
{
  if (isAce()) {
    return 1;
  }
  return value();
}

int BlackJackCard::maxValue()
{
  if (isAce()) {
    return 11;
  }
  return value();
}