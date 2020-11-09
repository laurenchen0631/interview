#include <string>

#ifndef USER_H
#define USER_H

class User {
public:
  User(int, std::string, int accountType);
  void renewMembership();

  int getID();
  void setID(int);

  std::string getDetails();
  void setDetails(std::string);

  int getAccountType();
  void setAccountType(int);

private:
  int id;
  std::string details;
};

#endif