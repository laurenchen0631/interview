#include "User.hh"
#include "Book.hh"


#ifndef BOOK_H
#define BOOK_H

class Display {
public:
  void displayUser(User* user);
  void displayBook(Book* book);
  void turnPageForward();
  void turnPageBackward();
  void refreshUsername();
  void refreshTitle();
  void refreshDetails();
  void refreshPage();

private:
  Book* activeBook;
  User* activeUser;
  int pageNumber {0};
};

#endif
