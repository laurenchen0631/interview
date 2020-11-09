#include <vector>
#include <string>

class ParkingSpot;

class Vehicle {
public:
  enum class Size: int { Motorcycle, Compact, Large };
  Size getSize();
  void partInSpot(ParkingSpot s) { parkingSpots.push_back(s); }
  void clearSpots();
  virtual bool canFitInSpot(ParkingSpot spot);
protected:
  std::vector<ParkingSpot> parkingSpots;
  std::string licensePlate;
  int spotsNeeded;
  Size size;
};

class Bus : public Vehicle {
public:
  Bus() {
    spotsNeeded = 5;
    size = Size::Large;
  }

  bool canFitInSpot(ParkingSpot spot);
};

class Car : public Vehicle {
public:
  Car() {
    spotsNeeded = 1;
    size = Size::Compact;
  }

  bool canFitInSpot(ParkingSpot spot);
};

class Motorcycle : public Vehicle {
public:
  Motorcycle() {
    spotsNeeded = 1;
    size = Size::Motorcycle;
  }

  bool canFitInSpot(ParkingSpot spot);
};

class ParkingSpot {
public:
  ParkingSpot(int r, int n, Vehicle::Size s);
  bool isAvailable();
  bool canFitVehicle(Vehicle vehicle);
  bool park(Vehicle v);
  int getRow();
  int getSpotNumber();
  void removeVehicle();
private:
  Vehicle vehicle;
  Vehicle::Size spotSize;
  int row;
  int spotNumber;
};