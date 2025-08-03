#!/usr/bin/env python3


L = [2,3,4,5,6]

new_list = list(map(lambda x:x if x%2 == 0 , L))
print(new_list)

