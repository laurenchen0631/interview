#include <unordered_map>
#include <string>
#include "Book.hh"

class Library {
public:
  Book* addBook(int id, std::string details);
  bool remove(Book*);
  bool remove(int);
  Book* find(int);
private:
  std::unordered_map<int, Book*> books;
};