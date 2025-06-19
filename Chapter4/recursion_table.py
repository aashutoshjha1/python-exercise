#!/usr/bin/env python3

def power_table(num, table):
   if table == 0:
      return 1
   if table > 0:
          return num * power_table(num, table-1)
           

print(power_table(2, 6))

