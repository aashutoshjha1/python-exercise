#!/usr/bin/env python3

try:
    x = 1 / 0
except Exception as e:
    print(f"Can't divide by zero! {e}")
finally:
    print("This will always run.")