class Bottle:
  def __init__(self, id) -> None:
    self.__poisoned = False
    self.__id = id

  def id(self):
    return self.__id

  def poison(self):
    self.__poisoned = True

  def is_poisoned(self) -> bool:
    return self.__poisoned

class Strip:
  DAYS_FOR_RESULTS = 7

  def __init__(self, id) -> None:
    self.__id = id
    self.__drops_by_day: list[list[Bottle]] = []

  def id(self):
    return self.__id

  def __resize_drops(self, day):
    while len(self.__drops_by_day) <= day:
      self.__drops_by_day.append([])

  def add_drops_on_day(self, day, bottle):
    self.__resize_drops(day)
    self.__drops_by_day[day].append(bottle)

  def __has_poison(self, bottles):
    for b in bottles:
      if b.is_poisoned():
        return True
    return False

  def is_positive_on_day(self, day):
    test_day = day - Strip.DAYS_FOR_RESULTS
    if test_day < 0 or test_day >= len(self.__drops_by_day):
      return False
    for d in range(test_day):
      bottles = self.__drops_by_day[d]
      if self.__has_poison(bottles):
        return True
    return False

def find_poisoned_bottle(bottles, strips):
  run_test(bottles, strips)
  positive = get_result(strips, 7)
  return set_bits(positive)

def run_test(bottles, strips):
  for bottle in bottles:
    id = bottle.id()
    bit_index = 0
    while id > 0:
      if id & 1:
        strips[bit_index].add_drops_on_day(0, bottle)
      bit_index += 1
      id >>= 1

def get_result(strips, day):
  positive = []
  for strip in strips:
    if strip.is_positive_on_day(day):
      positive.append(strip.id())
  return positive

def set_bits(positive):
  id = 0
  for bit_index in positive:
    id |= (1 << bit_index)
  return id