#include "Card.hh"

Card::Card(int c, Suit s): faceValue{c}, suit{s} {}

int Card::value()
{
  return faceValue;
}

Card::Suit Card::getSuit()
{
  return suit;
}