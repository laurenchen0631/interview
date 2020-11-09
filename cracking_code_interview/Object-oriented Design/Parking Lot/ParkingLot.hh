#include <array>
#include "Vehicle.hh";

template <std::size_t>
class Level;

class ParkingSpot;

class ParkingLot {
public:
  ParkingLot();
  bool parkVehicle(Vehicle vehicle);
private:
  static constexpr int NUM_LEVEL = 5;
  static constexpr int SPOTS_PER_LEVEL = 100;
  std::array<Level<SPOTS_PER_LEVEL>, NUM_LEVEL> levels;
};

template <std::size_t N>
class Level {
public:
  Level(int flr);
  int availableSpots();
  bool parkVehicle(Vehicle);
  bool parkStartingAtSpot(int num, Vehicle v);
  int findAvailableSpots(Vehicle vehicle);
  void spotFreed();

private:
  constexpr static int SPOTS_PER_ROW = 10;
  int floor;
  std::array<ParkingSpot, N> spots;
  int availableSpots {0};
};

