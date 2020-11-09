#include "CallCenter.hh"


CallCenter::CallCenter(std::array<vector<Employee>, EMPLOYEE_LEVEL> emp)
  :employees {emp}
{
}

void CallCenter::dispatchCall(Call call)  
{
  auto emp = getHandlerForCall(call);
  if (emp != nullptr) {
    emp->receiveCall(call);
    call.setHandler(emp);
  }
  else {
    call.reply("Please wait");
    callQueues[static_cast<int>(call.getRank())].push(call);
  }
}