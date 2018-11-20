#!/usr/bin/env python3

try: 
   n = int(input('number: '))
   result = 100 / n
   print(result)
except ValueError:
   print('invalid number')
except ZeroDivisionError:
   print('0 not allowed')
except (KeyboardInterrupt,EOFError):
   print('Bye-bye')

print('Done')   
