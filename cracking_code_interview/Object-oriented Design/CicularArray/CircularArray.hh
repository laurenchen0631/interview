#include <array>

template<typename T>
class Iterator {
public:
  Iterator<T> operator++(); // prefix ++
  Iterator<T> operator++(int); // postfix ++
  T& operator*() { return *current_position; }
private:
  T* begin;
  T* end;
  T* current_position;
  std::size_t size;
};

template<typename T, std::size_t N>
class CircularArray {
public:
  using value_type = T;
  void rotate(int shift);
  const T& operator[] (const int&) const; // search
  T& operator[](const int&); // assign
  Iterator<T> begin();
  Iterator<T> end();
private:
  std::array<T, N> items {};
  int head {0};
  // Iterator<T> iter;

  int convert(int);
};
