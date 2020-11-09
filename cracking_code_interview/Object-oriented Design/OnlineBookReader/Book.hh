#include <string>

class Book {
public:
  // Book(int, std::string);
  int getID();
  void setID(int);

  std::string getDetails();
  void setDetails(std::string);
private:
  int id;
  std::string details;
};