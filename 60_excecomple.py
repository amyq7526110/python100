#!/usr/bin/env python3



try: 
    n = int(input('number: '))
    result = 100 / n
except (ValueError,ZeroDivisionError):    
    print('invalid number')
except (KeyboardInterrupt,EOFError):    
    print('\n Bye-bye')
else:
    print(result)
finally:
    print('\033[31mDone\033[0m')

# 常用形式有try-except和try-finally
