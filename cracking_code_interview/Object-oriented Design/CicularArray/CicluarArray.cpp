#include "CircularArray.hh"


template<typename T, std::size_t N>
int CircularArray<T,N>::convert(int index)
{
  if (index < 0) {
    index += items.max_size();
  }

  return (head + index) % items.max_size();
}

template<typename T, std::size_t N>
void CircularArray<T,N>::rotate(int shift)
{
  head = convert(shift);
}

template<typename T, std::size_t N>
const T& CircularArray<T,N>::operator[] (const int& index) const
{
  int i = convert(index);
  return items[i];
}

template<typename T, std::size_t N>
T& CircularArray<T,N>::operator[](const int& index)
{
  int i = convert(index);
  return items[i];
}

template<typename T, std::size_t N>
Iterator<T> CircularArray<T,N>::begin()
{
  return Iterator<T> {items.begin(), items.end(), items.begin() + head};
}

template<typename T, std::size_t N>
Iterator<T> CircularArray<T,N>::end()
{
  return Iterator<T> {items.begin(), items.end(), items.begin() + convert(items.max_size() - 1)};
}

template<typename T>
Iterator<T> Iterator<T>::operator++()
{
  Iterator<T> old {*this};
  if (current_position == end) {
    current_position = begin;
  }
  else {
    ++current_position;
  }
  return old;
}

template<typename T>
Iterator<T> Iterator<T>::operator++(int junk)
{
  if (current_position == end) {
    current_position = begin;
  }
  else {
    ++current_position;
  }
  return *this;
}