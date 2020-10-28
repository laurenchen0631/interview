def draw_line(screen: list, width, x1: int, x2: int, y: int):

  start_offset = x1 % 8
  first_full_byte = x1 // 8
  if start_offset != 0:
    first_full_byte += 1
  
  end_offset = x2 % 8
  last_full_byte = x2 // 8
  if end_offset != 7:
    last_full_byte -= 1

  height =  width // 8
  for b in range(first_full_byte, last_full_byte + 1):
    screen[height * y + b] = 0xFF

  start_mask = 0xFF >> start_offset
  end_mask = ~(0xFF >> (end_offset + 1))

  if (p := x1 // 8) == x2 // 8:
    mask = start_mask & end_mask
    screen[height * y + p] |= mask
  else:
    if start_offset != 0:
      screen[height * y - first_full_byte - 1] |= start_mask
    if end_offset != 7:
      screen[height * y + last_full_byte + 1] |= end_mask

draw_line([0xff, 0xff], 8, 0, 4, 0)