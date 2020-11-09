#include <set>
#include "CDPlayer.hh"

class Jukebox {
public:
  Jukebox(CDPlayer, std::set<CD>);
  Song getCurrentSong();
  std::set<CD> getCollection();
  bool playCD();
  bool nextSong();
private:
  CDPlayer player;
  std::set<CD> collection;
};
