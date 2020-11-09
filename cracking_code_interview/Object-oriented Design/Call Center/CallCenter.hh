#include <vector>
#include <queue>
#include <string>
#include <array>

using std::vector;

class Employee;
class Call;

class CallCenter {
static constexpr int EMPLOYEE_LEVEL = 3;
public:
  CallCenter(std::array<vector<Employee>, EMPLOYEE_LEVEL>);
  void dispatchCall(Call);
  void hireEmployee(Employee);
private:
  std::array<vector<Employee>, EMPLOYEE_LEVEL> employees;
  std::array<std::queue<Call>, EMPLOYEE_LEVEL> callQueues;

  Employee* getHandlerForCall(Call);
  bool assignCall(Employee);
};

enum class Rank: int {Respondent, Manager, Director};

class Employee {  
public:
  Employee(CallCenter*, Rank);
  void receiveCall(Call);
  void finishCall();
  void escalateCall();
  Rank getRank();
  bool isFree();

private:
  std::string name;
  unsigned int id;
  Rank rank;
  bool busy;
  CallCenter* dispatcher;
};

class Call {
public:
  Call(std::string);
  void setHandler(Employee*);
  Rank getRank();
  void setRank();
  Rank incrementRank();
  void reply(std::string);
  void disconnect();
private:
  Rank rank; // A call can have no handler but have a rank
  Employee* handler;
  std::string caller;
};

class Director : public Employee {
public:
  Director(CallCenter* cc): Employee{cc, Rank::Director} {}
};

class Manager : public Employee {
public:
  Manager(CallCenter* cc): Employee{cc, Rank::Manager} {}
};

class Respondent : public Employee {
public:
  Respondent(CallCenter* cc): Employee{cc, Rank::Respondent} {}
};