import random

def gender_simulate(n: int) -> int:
  boys = 0
  girls = 0
  for _ in range(n):
    (num_boys, num_girls) = birth_simulate()
    boys += num_boys
    girls += num_girls

  return girls / boys

def birth_simulate():
  boys = 0
  girls = 0
  while girls == 0:
    if random.choice([0, 1]) == 0:
      girls += 1
    else:
      boys += 1
  return (boys, girls)

print(gender_simulate(1000))
