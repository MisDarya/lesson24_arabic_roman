from roman import *

t = ['IV', 'LVIII', 'MCMXCIV', 'XCIX', 'LXXX', 'LXIX']
print('\nИсходные данные: ', t)

print('\nКонвертируем из Римских в Арабские:')
for i in t:
  print(' ', i, '->' ,roman_to_int(i))

a=[4, 58, 1994, 26, 99, 69, 80, 101, 3456, 78]
print('\nКонвертируем из Арабских в Римские:')
for i in a:
  print(' ', i, '->',int_to_roman(i))

print('\nЗадача выполнена!\n')
