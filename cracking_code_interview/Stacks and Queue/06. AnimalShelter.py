from package.LinkedList import LinkedList

class SimpleAnimalShelter:
  CAT = 1
  DOG = 2

  def __init__(self):
    self.list = LinkedList([])

  def enqueue(self, animal):
    self.list.append(animal)

  def dequeue(self):
    oldest = self.list.head
    if oldest == None:
      raise Exception()
    self.list.head = self.list.head.next
    return oldest

  def dequeue_cat(self):
    return self.__dequeue_animal(SimpleAnimalShelter.CAT)

  def dequeue_dog(self):
    return self.__dequeue_animal(SimpleAnimalShelter.DOG)

  def __dequeue_animal(self, animal):
    if self.list.head == None:
      raise Exception()
    elif self.list.head.data == animal:
      tmp = self.list.head
      self.list.head = self.list.head.next
      return tmp

    oldest = None
    n = self.list.head
    while n.next != None and n.next.data != animal:
      n = n.next
    if n.next == None:
      raise Exception()
      
    oldest = n.next
    n.next = n.next.next
    return oldest

# shelter = SimpleAnimalShelter()
# shelter.enqueue(SimpleAnimalShelter.CAT)
# shelter.enqueue(SimpleAnimalShelter.CAT)
# shelter.enqueue(SimpleAnimalShelter.CAT)
# shelter.enqueue(SimpleAnimalShelter.CAT)
# shelter.enqueue(SimpleAnimalShelter.DOG)

# print(shelter.dequeue().data)
# print(shelter.dequeue_dog().data)
# print(shelter.dequeue_cat().data)
# print(shelter.dequeue_cat().data)
# print(shelter.dequeue_cat().data)

class Animal:
  def __init__(self, name):
    self._name = name
    self._timestamp = None
  
  @property
  def timestamp(self):
    return self._timestamp

  @timestamp.setter
  def timestamp(self, val):
    self._timestamp = val

  def __gt__(self, other):
    return self._timestamp < other.timestamp

class Cat(Animal):
  pass

class Dog(Animal):
  pass

class AnimalShelter:
  def __init__(self):
    self.cats = LinkedList([])
    self.dogs = LinkedList([])
    self.__stamp = 0
  
  def enqueue(self, animal: Animal):
    animal.timestamp = self.__stamp
    self.__stamp += 1

    if isinstance(animal, Cat):
      self.cats.append(animal)
    else:
      self.dogs.append(animal)

  def dequeue_any(self):
    if self.cats.head == None:
      return self.dequeue_dog()
    elif self.dogs.head == None:
      return self.dequeue_cat()

    dog = self.dogs.head.data
    cat = self.cats.head.data
    if (dog > cat):
      return self.dequeue_dog()
    else:
      return self.dequeue_cat()

  def dequeue_dog(self):
    if self.dogs.head == None:
      raise Exception()

    tmp = self.dogs.head.data
    self.dogs.head = self.dogs.head.next
    return tmp

  def dequeue_cat(self):
    if self.cats.head == None:
      raise Exception()

    tmp = self.cats.head.data
    self.cats.head = self.cats.head.next
    return tmp

s = AnimalShelter()
s.enqueue(Cat("c1"))
s.enqueue(Dog("d1"))
s.enqueue(Cat("c2"))
s.enqueue(Cat("c3"))
s.enqueue(Dog("d2"))
print(s.dequeue_any())
print(s.dequeue_any())
print(s.dequeue_dog())