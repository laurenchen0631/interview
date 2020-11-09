#include <vector>
#include "CD.hh"

class Playlist {
public:
  Song* getNextToPlay();
  void addSong(Song*);
private:
  Song* playing;
  std::vector<Song*> list;
};