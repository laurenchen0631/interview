def decimal_to_binary(num, limit = 64):
  if num >= 1 or num <= 0:
    return "ERROR"

  binary = ['.']
  val = 0.5
  for _ in range(limit):
    if num >= val:
      binary.append('1')
      num -= val
    elif num == 0:
      break
    else:
      binary.append('0')
    val /= 2

  if num != 0:
    return "ERROR"

  return ''.join(binary)

print(decimal_to_binary(0.72))