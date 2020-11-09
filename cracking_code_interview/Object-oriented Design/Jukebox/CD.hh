#include <string>
#include <fstream>
#include <vector>

class Song;

class CD {
private:
  std::string name;
  std::string artist;
  std::vector<Song> songs;
};

class Song {
public:
  Song(std::string uri);
private:
  std::string title;
  long durationMs;
  std::ifstream file;
  CD cd;
};