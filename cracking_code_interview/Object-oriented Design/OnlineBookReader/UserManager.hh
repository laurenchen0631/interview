#include <unordered_map>
#include <string>
#include "User.hh"

class UserManager {
public:
  User* addUser(int id, std::string details, int accountType);
  User* find(int);
  bool remove(User*);
  bool remove(int);
private:
  std::unordered_map<int, User*> books;
};