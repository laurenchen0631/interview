
class Card {
  enum class Suit : int {Club, Diamond, Heart, Spade};
protected:
  int faceValue;
  Suit suit;
public:
  Card(int, Suit);
  ~Card();

  virtual int value();

  Suit getSuit();
};