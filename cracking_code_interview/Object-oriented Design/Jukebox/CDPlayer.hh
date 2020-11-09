#include "Playlist.hh"

class CDPlayer {
public:
  Playlist getPlaylist();
  void setPlaylist(Playlist);

  CD getCD();
  void setCD(CD);
private:
  Playlist playlist;
  CD cd;
};