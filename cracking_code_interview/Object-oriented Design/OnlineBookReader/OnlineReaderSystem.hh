
#include "Library.hh"
#include "UserManager.hh"
#include "Display.hh"

class OnlineReaderSystem {
public:
  OnlineReaderSystem();
  ~OnlineReaderSystem();

  Library getLibrary();
  UserManager getUserManager();
  Display getDisplay();

  Book getActiveBook();
  void setActiveBook(Book);

  User getActiveUser();
  void setActiveUser(User);
  
private:
  Library* library;
  UserManager* userManager;
  Display* display;

  Book* activeBook;
  User* activeUser;
};